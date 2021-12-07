# おまじない処理
# IOS XEがHTTPSのために作成した自己発行証明書に対する警告を抑制することで、スクリプト実行時の見栄えをキレイにする
# 
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)





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
























'''
import requests

url = "https://webexapis.com/v1/messages"

payload="{\r\n  \"roomId\": \"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vN2VlNmVhNDAtNTc1Mi0xMWVjLWI0N2UtNDMxOGIyNGU0ODE1\",\r\n  \"text\": \"QoS change\"\r\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer MGM4YjA4MmYtMzI3YS00Y2QyLWE1ODUtYmM4NWY1NDM1ZDUyZmJmNTNmOWUtNzk0_P0A1_c98415b4-c72b-47aa-82ca-ffe96054cf5a'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

'''














'''

import requests

url = "https://webexapis.com/v1/messages"

payload="{\r\n  \"roomId\": \"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOTM4MjI1NTAtNTY1ZC0xMWVjLTk3MjQtMGI2N2JmNjg5MjEy\",\r\n  \"text\": \"Qos Change\"\r\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer MWJlNzg3YTYtZTQyNy00YmQ0LThhMzgtYjRjMmJhZWFmZDhjZTI2MjA4ODgtNmU0_P0A1_c98415b4-c72b-47aa-82ca-ffe96054cf5a'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)





import requests

url = "https://webexapis.com/v1/messages"

payload="{\r\n  \"roomId\": \"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZjFlMjVkYzAtNDY4ZC0xMWVjLTg1YTAtMmI1Y2QxMzA4YTY5\",\r\n  \"text\": \"setQoS.py complete!\"\r\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer NGUxYmQ4ZjYtNDAxMi00MTY1LTk1MTQtOTJmYjk4OWY2NDExZDAzMThlZDctMDdl_P0A1_c98415b4-c72b-47aa-82ca-ffe96054cf5a'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

'''
