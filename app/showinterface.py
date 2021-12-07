# おまじない処理
# IOS XEがHTTPSのために作成した自己発行証明書に対する警告を抑制することで、スクリプト実行時の見栄えをキレイにする
# 
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)




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
