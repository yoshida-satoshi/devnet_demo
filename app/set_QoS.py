
# おまじない処理
# IOS XEがHTTPSのために作成した自己発行証明書に対する警告を抑制することで、スクリプト実行時の見栄えをキレイにする
# 
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


# スクリプト実行時の見栄えを整えるための表示
print('----- Start change QoS ------')


# Router1 QoS RESTRICTED
import requests

url = "https://Router1.az.traino.cat/restconf/data/Cisco-IOS-XE-native:native/interface"

payload="{\r\n    \"Cisco-IOS-XE-native:interface\": {\r\n        \"GigabitEthernet\" : [\r\n            {\r\n                \"name\": \"1\",\r\n                \"Cisco-IOS-XE-policy:service-policy\": {\r\n                    \"output\": \"RESTRICTED\"\r\n                }\r\n            },\r\n                {\r\n                \"name\": \"2\",\r\n                \"Cisco-IOS-XE-policy:service-policy\": {\r\n                    \"input\": \"RESTRICTED\"\r\n                }\r\n            }\r\n        ]\r\n    }\r\n}"
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic aW5zdHJ1Y3RvcjppbnN0cnVjdG9yUGEkJHcwcmQ='
}

response = requests.request("PATCH", url, headers=headers, data=payload, verify=False)

# レスポンスの表示は不要であるため、見栄えを整えるためにprint文をコメントアウトする
# print(response.text)



# Router2 QoS RESTRICTED
import requests

url = "https://Router2.az.traino.cat/restconf/data/Cisco-IOS-XE-native:native/interface"

payload="{\r\n    \"Cisco-IOS-XE-native:interface\": {\r\n        \"GigabitEthernet\" : [\r\n            {\r\n                \"name\": \"2\",\r\n                \"Cisco-IOS-XE-policy:service-policy\": {\r\n                    \"output\": \"RESTRICTED\"\r\n                }\r\n            },\r\n                {\r\n                \"name\": \"3\",\r\n                \"Cisco-IOS-XE-policy:service-policy\": {\r\n                    \"input\": \"RESTRICTED\"\r\n                }\r\n            }\r\n        ]\r\n    }\r\n}"
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGVtbzpkZW1v'
}

response = requests.request("PATCH", url, headers=headers, data=payload, verify=False)

# レスポンスの表示は不要であるため、見栄えを整えるためにprint文をコメントアウトする
# print(response.text)


# スクリプト実行時の見栄えを整えるための表示
print('----- Complete change QoS ------')

