
import pytest
import base64
from main import extract_content, validate

@pytest.fixture
def check_env_vars():
    import os
    import re
    email_regex = re.compile(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
    assert 'USER_EMAIL' in os.environ
    assert re.match(email_regex, os.environ['USER_EMAIL'])

def test_extract_content():
    '''We can decode base64 string received from pubsub'''
    event = {
        "data": "eyJlbWFpbEFkZHJlc3MiOiAidXNlckBleGFtcGxlLmNvbSIsICJoaXN0b3J5SWQiOiAiOTg3NjU0MzIxMCJ9",
    }
    res = extract_content(event)
    assert res["emailAddress"] == "user@example.com"

def test_validate(check_env_vars):
    '''A valid data obj is validated'''
    data = {
        'emailAddress': 'ben.little6@gmail.com',
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
        'emailAddress': 'ben.little6@gmail.com',
        'butter': 'no',
    }
    assert not validate(data)

def test_validate_wrong_emailAddress(check_env_vars):
    '''An data obj with wrond emailAddress value is nixed'''
    data = {
        'emailAddress': 'testy.mctest@test.tests',
        'historyId': '123456789',
    }
    assert not validate(data)

