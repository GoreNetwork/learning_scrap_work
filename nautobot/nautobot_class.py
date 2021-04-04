import requests
from pprint import pprint
import requests
import json

token = 'b478aed09d3fecdb55f838e31185eb1584712cc3'

headers = {
    'accept': 'application/json',
    'Authorization': f'Token {token}'
}

ip = '192.168.174.10'
port = '8000'

response = requests.get(
    'http://192.168.174.10:8000/api/dcim/sites/', headers=headers)


class nautobot():
    def __init__(self, ip, headers, port):
        self.ip = ip
        self.headers = headers
        self.port = port
        self.manufacturer_data = self.build_manufacturer_data()

    def make_get_request(self, url):
        response = requests.get(
            f"http://{self.ip}:{self.port}/{url}", headers=headers)
        response.raise_for_status()
        return response.json()

    def make_post_request(self, url, data):
        # data = json.dumps(data)
        print("Data being posted: ")
        print(data)
        print('\n\n')
        print("Manufacturer Data: ")
        pprint(self.manufacturer_data)
        print('\n\n')
        response = requests.post(
            f"http://{self.ip}:{self.port}/{url}", headers=headers, data=data)
        pprint(response.json())
        response.raise_for_status()
        return response.json()

    def get_sites(self):
        url = "api/dcim/sites/"
        sites = self.make_get_request(url)
        return sites

    def create_site(self, site_name):
        site_data = {
            "name": site_name,
            "slug": site_name,
            "status": "active", }
        url = "api/dcim/sites/"
        self.make_post_request(url, site_data)

    def create_manufacturer(self, manufacturer):
        manufacturer_data = {
            "name": manufacturer,
            "slug": manufacturer,
            "description": manufacturer, }
        url = "api/dcim/manufacturers/"
        self.make_post_request(url, manufacturer_data)

    def build_manufacturer_data(self):
        manufacturer_data = {}
        manufacturer_raw = self.get_manufacturer()
        for each in manufacturer_raw['results']:
            manufacturer_data[each['name']] = each['id']
        return manufacturer_data

    def get_manufacturer(self):
        url = "api/dcim/manufacturers/"
        sites = self.make_get_request(url)
        return sites

    def make_sure_site_exists(self, site_name):
        sites = self.get_sites()['results']
        exists = False
        for site in sites:
            if site['name'] == site_name:
                exists = True
        if exists == False:
            self.create_site(site_name)
        return True

    def make_sure_manufacturer_exists(self, manufacturer_name):
        manufacturers = self.get_manufacturer()['results']
        exists = False
        for manufacturer in manufacturers:
            if manufacturer['name'] == manufacturer_name:
                exists = True
        if exists == False:
            self.create_manufacturer(manufacturer_name)
        return True

    def make_sure_device_type_exists(self, device_type_data):
        device_type_name = device_type_data['name']
        device_types = self.get_device_type()['results']
        exists = False
        for device_type in device_types:
            if device_type['model'] == device_type_name:
                exists = True
        if exists == False:
            self.create_device_type(device_type_data)
        return True

    def get_device_type(self):
        url = "api/dcim/device-types"
        sites = self.make_get_request(url)
        return sites

    def create_device_type(self, device_type_data):
        if device_type_data['manufacturer'] not in self.manufacturer_data:
            self.manufacturer_data = self.build_manufacturer_data()
        device_type_data = {
            "manufacturer": self.manufacturer_data[device_type_data['manufacturer']],
            "slug": device_type_data['name'],
            "model": device_type_data['name'],
        }
        url = "api/dcim/device-types/"

        self.make_post_request(url, device_type_data)


home_box = nautobot(ip, headers, port)

# pprint(home_box.make_sure_site_exists("Himes_House"))
# pprint(home_box.make_sure_site_exists("Ted"))
# pprint(home_box.make_sure_manufacturer_exists("VM"))
# pprint(home_box.make_sure_manufacturer_exists("Cisco"))

manufacturer_data = home_box.manufacturer_data

device_type_data = {
    'name': 'fake1',
    'manufacturer': 'Cisco'

}
pprint(home_box.make_sure_device_type_exists(device_type_data))
