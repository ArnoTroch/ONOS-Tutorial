import sys
import csv
import requests

# REST API url and headers
host = "192.168.0.239"
port = "8181"
username = "karaf"
password = "karaf"
url = f"http://{host}:{port}/onos/v1/acl/rules"
headers = {'Content-type': 'application/json'}

# read policy file
policyFile = "firewall-policies.csv"
firewall_rules = []
with open(policyFile, 'r') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in rows:
        if line_count == 0:
            line_count += 1
            continue
        firewall_rules.append((row[1], row[2]))
        line_count += 1

# put each firewall rule into the ACL using the REST API
for rule in firewall_rules:
    resp = requests.post(
        url,
        json={
            "srcIp": "10.0.0.0/24",
            "srcMac": rule[0],
            "dstMac": rule[1]
        },
        auth=(username, password)
    )
    print(resp.text)

