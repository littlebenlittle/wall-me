
import pytest
import base64
from main import extract_content

def test_extract_content():
    event = {
        "data": "eyJlbWFpbEFkZHJlc3MiOiAidXNlckBleGFtcGxlLmNvbSIsICJoaXN0b3J5SWQiOiAiOTg3NjU0MzIxMCJ9",
    }
    res = extract_content(event)
    assert "emailAddress" in res

