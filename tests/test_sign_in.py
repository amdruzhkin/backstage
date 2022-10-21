import json

import pytest
import requests

HOST = 'http://127.0.0.1:8000'
@pytest.mark.parametrize(
    "login, email, password, code", [
        ('test_user', None, 'test_user_password', 200),
        (None, 'test_user@gmail.com', 'test_user_password', 200),
        (None, None, 'test_user_password', 422),
        ('test_user404', 'test_user404@gmail.com', 'test_user404_password', 404),
    ]
)
def test_sign_in(login, email, password, code):
    url = HOST + '/auth/sign_in'

    payload = dict()

    if login is not None:
        payload['login'] = login
    elif email is not None:
        payload['email'] = email

    payload['password'] = password

    response = requests.post(url=url, data=json.dumps(payload))
    print(response.text)
    assert response.status_code == code

