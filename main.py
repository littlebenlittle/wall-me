
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

def get_token(uri):
    from google.cloud import storage
    import re
    s = re.compile(r'gs://([a-zA-Z0-9]+)/(.+)')
    m = s.match(uri)
    client = storage.Client()
    bucket = client.bucket(m.group(1))
    blob   = bucket.blob(m.group(2))
    content = blob.download_as_string()
    data = json.loads(content)
    from google.oauth2.credentials import Credentials
    creds = Credentials(
        token=data['token'],
        refresh_token=data['refresh_token'],
        token_uri=data['token_uri'],
        client_secret=data['client_secret'],
        client_id=data['client_id'],
        scopes=data['scopes'],
    )
    return creds

def get_gmail():
    from googleapiclient.discovery import build
    creds = get_token('gs://wallme/v1/token.json')
    gmail = build('gmail', 'v1', credentials=creds)
    return gmail

def wallme(event, context):
    data = extract_content(event)
    if not validate(data):
        return
    historyId = data['historyId']

