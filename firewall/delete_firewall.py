import requests

# REST API url and headers
host = "192.168.0.239"
port = "8181"
username = "karaf"
password = "karaf"
url = f"http://{host}:{port}/onos/v1/acl/rules"

# remove all rules from the ACL using the REST API
resp = requests.delete(url, auth=(username, password))
print(resp.text)
