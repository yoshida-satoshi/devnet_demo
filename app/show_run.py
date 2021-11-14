# Webex Teams show run
import requests
import json


import cli

showrun = cli.execute("show run int gi1")

payload={"roomId":"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNzBlNWYwZTAtNDQ5Yi0xMWVjLTkxMzEtMWRlMmQ0OThhM2Ey","text":"{}".format(showrun)}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer MTE0Njc4OTktYThlMi00MTEwLWIxNmMtZGUzNWEzNGM1MjM1YzhmMWJlMTMtMDYw_P0A1_c98415b4-c72b-47aa-82ca-ffe96054cf5a'
}

url = "https://webexapis.com/v1/messages"

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
