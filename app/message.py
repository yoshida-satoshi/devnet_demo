import requests
import json

token  = 'OGZlODIwMWYtZjc0ZC00NzQxLWIxNzMtMWNjNGRlZmU0MmZmYWY2ZTUzMGItNWVk_PF84_consumer'
roomid = 'Y2lzY29zcGFyazovL3VzL1JPT00vOGVhZTVlYjAtMmY2NC0xMWVjLThkMWQtNzliZDE4YzM5OGY1'

def get_message(request, msgid=None):

    if request != None:
        webhook_notify = json.loads(request.data.decode('utf-8'))
        msgid=webhook_notify['data']['id']

    url = f'https://api.ciscospark.com/v1/messages/{msgid}'

    payload={}
    headers = {'Accept': 'application/json','Authorization': f'Bearer {token}'}

    response = requests.get(url, headers=headers, data=payload)

    return response.json()['text']

def send_message(message):
    url = "https://api.ciscospark.com/v1/messages"

    payload=json.dumps({"roomId":roomid, "text":message})
    headers = {'Accept': 'application/json','Content-Type': 'application/json','Authorization': f'Bearer {token}' }
    response = requests.post(url, headers=headers, data=payload)

    return response
