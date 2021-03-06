
import pytest
import base64
import Courier
from main import extract_content, validate, get_gmail, get_token, wallme
from googleapiclient.discovery import Resource

@pytest.fixture
def USER_EMAIL():
    import os
    import re
    email_regex = re.compile(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
    assert 'USER_EMAIL' in os.environ
    assert re.match(email_regex, os.environ['USER_EMAIL'])
    return os.environ['USER_EMAIL']

@pytest.fixture
def gmail():
    return get_gmail()

def test_extract_content():
    '''We can decode base64 string received from pubsub'''
    pubsub_event = { "data": "eyJlbWFpbEFkZHJlc3MiOiAidXNlckBleGFtcGxlLmNvbSIsICJoaXN0b3J5SWQiOiAiMTIzNDU2Nzg5In0=" }
    res = extract_content(pubsub_event)
    assert res["emailAddress"] == "user@example.com"

def test_validate(USER_EMAIL):
    '''A valid data obj is validated'''
    data = {
        'emailAddress': USER_EMAIL,
        'historyId': '123456789',
    }
    assert validate(data)

# TODO: fix typos in docstrings 2020-02-25T10:28:13Z
def test_validate_no_emailAddress():
    '''An data obj with no emailAddress key is nixed'''
    data = {
        'butter': 'yes',
        'historyId': '123456789',
    }
    assert not validate(data)

def test_validate_no_historyId():
    '''An data obj with no historyId key is nixed'''
    data = {
        'emailAddress': USER_EMAIL,
        'butter': 'no',
    }
    assert not validate(data)

def test_validate_wrong_emailAddress(USER_EMAIL):
    '''An data obj with wrond emailAddress value is nixed'''
    data = {
        'emailAddress': 'testy.mctest@test.tests',
        'historyId': '123456789',
    }
    assert not validate(data)

@pytest.mark.skip(reason='this is an integration test')
def test_get_token():
    '''We can get the token from storage'''
    uri = 'gs://wallme/v1/token.json'
    token = get_token(uri)
    import hashlib
    m = hashlib.sha256()
    m.update(token.client_id.encode('utf8'))
    m.update(token.client_secret.encode('utf8'))
    assert m.digest() == b'\xe1\xcds\x05\x01)BQ\x840\x18\x8e\x8fh\xce\x8e\xe8\xec\x7f\xc6A\xfc\xc1wn\xed\x0b\xb7g\xa26K'

@pytest.mark.skip(reason='this is an integration test')
def test_get_gmail(gmail):
    '''We can build the gmail client'''
    assert gmail
    assert isinstance(gmail, Resource)

def test_wallme():
    '''Wallme successfully sends a message'''
    pubsub_event = { "data": "eyJlbWFpbEFkZHJlc3MiOiAidXNlckBleGFtcGxlLmNvbSIsICJoaXN0b3J5SWQiOiAiMTIzNDU2Nzg5In0=" }
    wallme(pubsub_event, None)
    sent_message = \
"""
from: user@example.com

⭐ This message contains
\tmultiple lines.
"""
    assert sent_message in Courier.bag

def test_wallme_2():
    '''Wallme successfully sends another message'''
    pubsub_event = { "data": "eyJlbWFpbEFkZHJlc3MiOiAib3RoZXJAbm93aGVyZS5uZXQiLCAiaGlzdG9yeUlkIjogIjk4NzY1NDMyMSJ9" }
    wallme(pubsub_event, None)
    sent_message = \
"""
from: other@nowhere.net

This is just a regular old message
"""
    assert sent_message in Courier.bag

def test_Courier():
    '''We can attach messages to the Courier'''
    message = "test message"
    Courier.attach(message)
    assert message in Courier.bag

