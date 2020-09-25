import requests


def test_post_login():
    url = 'http://qa.yansl.com:8084/login/'
    headers = {"Content-Type": "application/json"}
    data = {
            "pwd": "wsx666666",
            "userName": "wsx6666"
            }
    r = requests.request("POST", url=url, json=data, headers=headers)
    print(r.text)
    token = r.json()['data']['token']
    print(token)
    return token


def test_post_acclock():
    url = "http://qa.yansl.com:8084/acc/accLock"
    data = {"accountName": "wuxian3242"}
    r = requests.request("POST", url=url, data=data)
    print(r.text)


def test_post_lock():
    url = 'http://qa.yansl.com:8084/user/lock'
    headers = {"token":"token"}
    data = {"userName": "wuxian3242"}
    r = requests.request("POST", url=url, data=data, headers=headers)
    print(r.text)


def test_poet_flie():
    data = {"file": open("test.xls", "rb")}
    headers = { "token": "token"}
    r = requests.request("POST", "http://qa.yansl.com:8084/product/uploaProdRepertory", files=data, headers=headers)
    print(r.text)
