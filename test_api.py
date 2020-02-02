import unittest
import pytest
from hello import app, _sum

# run the tests: pytest test_api.py --disable-pytest-warnings

def test_sum():
    assert _sum(1, 2) == '3'

def test_successful_api_call():
    client = app.test_client()
    response = client.get('/?a=1&b=2')
    assert response.status_code == 200

def test_mandatory_params():
    client = app.test_client()
    response = client.get('/?a=wrong&b=parameters')
    assert response.status_code == 400

def test_missing_params():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 400

def test_only_get_is_allowed():
    client = app.test_client()
    response = client.post('/')
    assert response.status_code == 405
