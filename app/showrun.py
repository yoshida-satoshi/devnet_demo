
import cli

show_run = cli.execute("show run int gi1")

import requests
import json

url = "https://webexapis.com/v1/messages"

payload={"roomId":"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZjFlMjVkYzAtNDY4ZC0xMWVjLTg1YTAtMmI1Y2QxMzA4YTY5","text":show_run}

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer NGUxYmQ4ZjYtNDAxMi00MTY1LTk1MTQtOTJmYjk4OWY2NDExZDAzMThlZDctMDdl_P0A1_c98415b4-c72b-47aa-82ca-ffe96054cf5a'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text)