
import cli

show_run = cli.execute("show run int gi1")

import requests
import json

url = "https://webexapis.com/v1/messages"

payload={"roomId":"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOTM4MjI1NTAtNTY1ZC0xMWVjLTk3MjQtMGI2N2JmNjg5MjEy","text":show_run}

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer MWJlNzg3YTYtZTQyNy00YmQ0LThhMzgtYjRjMmJhZWFmZDhjZTI2MjA4ODgtNmU0_P0A1_c98415b4-c72b-47aa-82ca-ffe96054cf5a'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text)