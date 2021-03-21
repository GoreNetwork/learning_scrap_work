

import pandas as pd
from pybatfish.client.commands import *
from pybatfish.datamodel import *
from pybatfish.datamodel.answer import *
from pybatfish.datamodel.flow import *
from pybatfish.question import *
from pybatfish.question import bfq
from pprint import pprint
import json


# Docker host running
# docker run --name batfish -v batfish-data:/data -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone
# Once you have run this once to start it back up you'll need to run "docker start [huge ID line]"
bf_session.host = '192.168.174.129'
print(1)
load_questions()
print(2)
network_name = 'lab'
snapshot_path = 'D:\\github\\learning_scrap_work\\batfish work\\snapshots\{}\\'.format(
    network_name)
print(3)
bf_set_network(network_name)
print(4)
bf_session.init_snapshot(snapshot_path, name=network_name, overwrite=True)
print(5)

# .frame makes it into pandas data.... wish I knew pandas
# pprint(dir(bfq))
# print(bfq.routes().answer().frame())

# How did the parsing go?
# pprint(bfq.fileParseStatus().answer().frame())
# What failed?  (something alwasy fails)
# pprint(bfq.parseWarning().answer().frame())

# Find duplicate IPs
# pprint(bfq.ipOwners(duplicatesOnly=True).answer().frame())
# See Data per row abit clearer
# pprint(bfq.ipOwners(duplicatesOnly=True).answer().frame().iloc[0])


def ip_flow_validation(bfq, src_ip, dst_ip, start_device,  end_dev=""):
    pprint(src_ip)
    return bfq.reachability(
        pathConstraints=PathConstraints(
            startLocation=start_device, endLocation=end_dev),
        headers=HeaderConstraints(srcIps=src_ip, dstIps=dst_ip),
        actions="SUCCESS,FAILURE"
    ).answer().frame()


ip_tests = [
    {'src_ip': '172.16.1.1',
     'dst_ip': '172.19.0.12',
     'start_device': 'office_switch', },
    {'src_ip': '172.16.1.1',
     'dst_ip': '172.19.0.1',
     'start_device': 'office_switch', },
]


def test_ip_flows(ip_tests):
    for test in ip_tests:
        results = ip_flow_validation(bfq, test['src_ip'],
                                     test['dst_ip'], test['start_device'])
        # pprint(dir(results))
        # pprint(results.dict())
        # pprint(results.dict()['status'])
        print(results.to_json())
        print('\n')


def port_flow_validation(bfq, src_ip, dst_ip, start_device, dst_port,  end_dev=""):
    pprint(src_ip)
    return bfq.reachability(
        pathConstraints=PathConstraints(
            startLocation=start_device, endLocation=end_dev),
        headers=HeaderConstraints(
            srcIps=src_ip, dstIps=dst_ip, dstPorts=dst_port,
            ipProtocols=[
                "UDP",
                "TCP"
            ]),
        actions="SUCCESS,FAILURE"
    ).answer().frame()


port_tests = [
    {'src_ip': '172.16.1.1',
     'dst_ip': '172.19.0.12',
     'start_device': 'office_switch',
     'dst_port': '23'},
    {'src_ip': '172.16.1.1',
     'dst_ip': '172.19.0.12',
     'start_device': 'office_switch',
     'dst_port': '22'},
]


def test_port_flows(port_tests):
    all_results = []
    for test in port_tests:
        results = port_flow_validation(bfq, test['src_ip'],
                                       test['dst_ip'], test['start_device'], test['dst_port'])
        # pprint(dir(results))
        # pprint(results.dict())
        # pprint(results.dict()['status'])
        all_results.append(results)
        # pickle_data(results, 'pickle_data.pickle')
        # json_data = results.to_json()
        # json1_data = json.loads(json_data)
        # pprint(json1_data)

    return all_results


def pickle_data(data_frame, file_name):
    data_frame.to_pickle(file_name)


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


results = test_port_flows(port_tests)
for result in results:
    data = result.to_json()
    data = json.loads(data)
    pprint(data)
    print(result)

print(results)
