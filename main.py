import requests

emulator_url = 'http://127.0.0.1:54510/v1/projects/testbed-test:lookup'

payload = b'{"keys": [{"partitionId": {"projectId": "testbed-test", "namespaceId": ""}, "path": [{"kind": "TestEntity", "id": "5348024557502464"}]}], "readOptions": {"newTransaction": {"readWrite": {}}}}'

headers = {'Content-Length': '191', 'Content-Type': 'application/json'}

# POST request to the emulator
resp = requests.post(emulator_url, headers=headers, data=payload)

# check response's data
data = resp.json()

# data must include "transaction" because payload has "readOptions": {"newTransaction": {"readWrite": {}}}, but it doesn't include the "transaction".

print(data)