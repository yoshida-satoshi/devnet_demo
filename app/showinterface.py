import requests

url = "https://Router1.az.traino.cat/restconf/data/Cisco-IOS-XE-native:native/interface"

payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGVtbzpQYSQkdzByZA=='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

