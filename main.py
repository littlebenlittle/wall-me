
import os
import base64
import json
import logging

def extract_content(event):
    s = base64.b64decode(event['data']).decode('utf-8')
    j = json.loads(s)
    return j

def validate(data):
    missing  = []
    expected = [ 'emailAddress', 'historyId' ]
    for k in expected:
        if k not in data:
            missing.append(k)
    if len(missing) > 0:
        return 0 
    if data['emailAddress'] != os.environ['USER_EMAIL']:
        return 0
    return 1

def wallme(event, context):
    data = extract_content(event)
    if not validate(data):
        return
    historyId = data['historyId']

