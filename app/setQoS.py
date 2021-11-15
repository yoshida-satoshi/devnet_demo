

# router1

import requests

url = "https://Router1.az.traino.cat/restconf/data/Cisco-IOS-XE-native:native/interface"

payload="{\r\n    \"Cisco-IOS-XE-native:interface\": {\r\n        \"GigabitEthernet\" : [\r\n            {\r\n                \"name\": \"1\",\r\n                \"Cisco-IOS-XE-policy:service-policy\": {\r\n                    \"output\": \"RESTRICTED\"\r\n                }\r\n            },\r\n                {\r\n                \"name\": \"2\",\r\n                \"Cisco-IOS-XE-policy:service-policy\": {\r\n                    \"input\": \"RESTRICTED\"\r\n                }\r\n            }\r\n        ]\r\n    }\r\n}"
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGVtbzpQYSQkdzByZA=='
}

response = requests.request("PATCH", url, headers=headers, data=payload,verify=False)

print(response.text)


# router2
import requests

url = "https://Router2.az.traino.cat/restconf/data/Cisco-IOS-XE-native:native/interface"

payload="{\r\n    \"Cisco-IOS-XE-native:interface\": {\r\n        \"GigabitEthernet\" : [\r\n            {\r\n                \"name\": \"2\",\r\n                \"Cisco-IOS-XE-policy:service-policy\": {\r\n                    \"output\": \"RESTRICTED\"\r\n                }\r\n            },\r\n                {\r\n                \"name\": \"3\",\r\n                \"Cisco-IOS-XE-policy:service-policy\": {\r\n                    \"input\": \"RESTRICTED\"\r\n                }\r\n            }\r\n        ]\r\n    }\r\n}"
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGVtbzpQYSQkdzByZA=='
}

response = requests.request("PATCH", url, headers=headers, data=payload,verify=False)

print(response.text)
