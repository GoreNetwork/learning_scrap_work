import os
import re
import socket
import sys
import netmiko
from getpass import getpass
from ciscoconfparse import CiscoConfParse
from pprint import pprint
import ipaddress
import time
import json
from pprint import pprint


def write_json_file(file_name, data):
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)


def send_command(net_connect, command):
    return net_connect.send_command_expect(command)


def make_connection(ip, username, password):
    try:
        net_connect = netmiko.ConnectHandler(
            device_type='cisco_ios', ip=ip, username=username, password=password)
        output = net_connect.send_command_expect("show ver")
        # print (output)
        if "Nexus" in output:
            net_connect.disconnect()
            return netmiko.ConnectHandler(device_type='cisco_nxos', ip=ip, username=username, password=password)
        return net_connect
    except:
        try:
            return netmiko.ConnectHandler(device_type='cisco_ios_telnet', ip=ip, username=username, password=password)
        except:
            issue = ip + ", can't be ssh/telneted to"
            to_doc_a("Issues.csv", issue)
            to_doc_a("Issues.csv", '\n')
            return None


def get_ip(input):
    return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))


def read_in_file(file_name):
    file_obj = open(file_name, "r")
    output = file_obj.read()
    return output


def to_doc_w(file_name, varable):
    f = open(file_name, 'w')
    f.write(varable)
    f.close()


username = 'dhimes'
password = 'password'
file_name = "IPs.txt"
hosts_file_name = 'hosts.csv'

file_data = read_in_file(file_name)

ips = get_ip(file_data)


def pull_hostname(running_config):
    for line in running_config.split('\n'):
        if 'hostname' in line:
            hostname = line.split(' ')[-1]
            hostname = hostname.rstrip('\n')
            return hostname


# Pull configs and put them in configs folder with their hostnames.cfg as the file name
for ip in ips:
    print(ip)
    connection = make_connection(ip, username, password)
    running_config = send_command(connection, 'show run')
    hostname = pull_hostname(running_config)+'.cfg'
    output_folder = 'snapshots/lab/configs'
    file_output = os.path.join(output_folder, hostname)
    to_doc_w(file_output, running_config)

# build hosts files

hosts_file_data = read_in_file(hosts_file_name).split('\n')
for host_file_data in hosts_file_data:
    host_file_data = host_file_data.split(',')
    #  got to watch out for empty lines
    if len(host_file_data) < 2:
        continue
    # pprint(host_file_data)
    output_file_data = {
        "hostname": host_file_data[0],
        "iptablesFile": host_file_data[1],
        "hostInterfaces": {
            host_file_data[2]: {
                "name": host_file_data[2],
                "prefix": host_file_data[3],
                "gateway": host_file_data[4]
            }
        }
    }
    output_folder = 'snapshots/lab/hosts'
    output_file_name = "{}.json".format(host_file_data[0])
    file_name = os.path.join(output_folder, output_file_name)
    write_json_file(file_name, output_file_data)
