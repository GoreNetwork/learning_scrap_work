from pprint import pprint
import requests

token = 'b478aed09d3fecdb55f838e31185eb1584712cc3'

headers = {
    # 'accept': 'text/plain',
    'accept': 'application/json',

    'Authorization': f'Token {token}'
}

data = {'manufacturer': "3709e262-b17e-4795-a5a4-11b904b885e1",
        "test": "fake", "model": "fake", "comments": "Poop on this!!", 'slug': 'fake'}

response = requests.post(
    'http://192.168.174.10:8000/api/dcim/device-types/', headers=headers, data=data
)
pprint(data)

print(response.json())
