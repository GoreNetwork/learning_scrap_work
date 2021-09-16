

import urllib.request
import urllib.error
import requests
from pytest_httpserver import HTTPServer


server = HTTPServer(port=4000)
server.expect_request("/foobar").respond_with_json({"foo": "bar"})
server.expect_request("/billybob").respond_with_json({"billy": "bob"})
server.start()
try:
    r = requests.get('http://127.0.0.1:4000/foobar')
    print(r.json())
    r = requests.get('http://127.0.0.1:4000/billybob')
    print(r.json())
except urllib.error.HTTPError as err:
    print(err)
    server.stop()

server.stop()
