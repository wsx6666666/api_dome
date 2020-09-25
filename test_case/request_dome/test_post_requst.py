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


def test_post_change():
    url = 'http://qa.yansl.com:8084/acc/changeBalance/{accountId}'.format(accountId=17906)
    headers = {"Content-Type": "application/json","token": "eyJ0aW1lT3V0IjoxNjAxMDI0OTE5NTk3LCJ1c2VySWQiOjE2MDk5LCJ1c2VyTmFtZSI6IndzeDY2NjYifQ=="}
    data ={
         "balance": 1000
        }
    r = requests.request("POST",url=url,json=data,headers=headers)
    print(r.text)
    assert "修改成功" in r.text


def test_post_charge():
    url ='http://qa.yansl.com:8084/acc/charge'
    headers ={"Content-Type": "application/json","token": "eyJ0aW1lT3V0IjoxNjAxMDI0OTE5NTk3LCJ1c2VySWQiOjE2MDk5LCJ1c2VyTmFtZSI6IndzeDY2NjYifQ=="}
    data ={
              "accountName": "wuxian9415",
              "changeMoney": 10
            }
    r = requests.request("POST",url=url,json=data,headers=headers)
    print(r.text)
    assert "扣款成功" in r.text

def test_post_seluser():
    url ='http://qa.yansl.com:8084/acc/selAllAccs/{pageNum}/{pageSize}'.format(pageNum=1,pageSize=10)
    headers ={"token": "eyJ0aW1lT3V0IjoxNjAxMDI0OTE5NTk3LCJ1c2VySWQiOjE2MDk5LCJ1c2VyTmFtZSI6IndzeDY2NjYifQ=="}
    r =requests.request("POST",url=url,headers=headers)
    print(r.text)
    assert "查询成功" in r.text