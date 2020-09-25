import requests


# def test_post_login():
#     url = 'http://qa.yansl.com:8084/login/'
#     headers = {"Content-Type": "application/json"}
#     data = {
#             "pwd": "wsx666666",
#             "userName": "wsx6666"
#             }
#     r = requests.request("POST", url=url, json=data, headers=headers)
#     print(r.text)
#     token = r.json()['data']['token']
#     print(token)
#     return token


def test_post_acclock():
    url = "http://qa.yansl.com:8084/acc/accLock"
    data = {"accountName": "wuxian3242"}
    r = requests.request("POST", url=url, data=data)
    print(r.text)


def test_post_lock():
    url = 'http://qa.yansl.com:8084/user/lock'
    headers = {"token":"eyJ0aW1lT3V0IjoxNjAxMDI0OTE5NTk3LCJ1c2VySWQiOjE2MDk5LCJ1c2VyTmFtZSI6IndzeDY2NjYifQ=="}
    data = {"userName": "wuxian3242"}
    r = requests.request("POST", url=url, data=data, headers=headers)
    print(r.text)
    assert "冻结成功" in r.text

def test_post_unlock():
    url ='http://qa.yansl.com:8084/user/unLock'
    headers = {"token":"eyJ0aW1lT3V0IjoxNjAxMDI0OTE5NTk3LCJ1c2VySWQiOjE2MDk5LCJ1c2VyTmFtZSI6IndzeDY2NjYifQ=="}
    data = {"userName":"wuxian3242"}
    r = requests.request("POST",url=url,data=data,headers=headers)
    print(r.text)
    assert "解冻成功" in r.text


def test_user_login():
    url ='http://qa.yansl.com:8084/login/'
    headers = {"Content-Type": "application/json"}
    data = {
          "pwd": "wsx123456",
          "userName": "wei666"
        }
    r =  requests.request("POST",url=url,json=data,headers=headers)
    print(r.text)
    assert "登录成功" in r.text
# def test_poet_flie():
#     data = {"file": open("test.xls", "rb")}
#     headers = { "token": "eyJ0aW1lT3V0IjoxNjAxMDI0OTE5NTk3LCJ1c2VySWQiOjE2MDk5LCJ1c2VyTmFtZSI6IndzeDY2NjYifQ=="}
#     r = requests.request("POST", "http://qa.yansl.com:8084/product/uploaProdRepertory", files=data, headers=headers)
#     print(r.text)



