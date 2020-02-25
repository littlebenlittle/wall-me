
import base64
import json

def extract_content(event):
    s = base64.b64decode(event['data']).decode('utf-8')
    j = json.loads(s)
    return j


def wallme(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    return pubsub_message

