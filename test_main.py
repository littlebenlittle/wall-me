
import pytest
import base64
from main import extract_content, validate, get_gmail_client
from googleapiclient.discovery import Resource

@pytest.fixture
def USER_EMAIL():
    import os
    import re
    email_regex = re.compile(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
    assert 'USER_EMAIL' in os.environ
    assert re.match(email_regex, os.environ['USER_EMAIL'])
    return os.environ['USER_EMAIL']

def test_extract_content():
    '''We can decode base64 string received from pubsub'''
    event = {
        "data": "eyJlbWFpbEFkZHJlc3MiOiAidXNlckBleGFtcGxlLmNvbSIsICJoaXN0b3J5SWQiOiAiOTg3NjU0MzIxMCJ9",
    }
    res = extract_content(event)
    assert res["emailAddress"] == "user@example.com"

def test_validate(USER_EMAIL):
    '''A valid data obj is validated'''
    data = {
        'emailAddress': USER_EMAIL,
        'historyId': '123456789',
    }
    assert validate(data)

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

def test_get_gmail_client():
    gmail = get_gmail_client()
    assert isinstance(gmail, Resource)

