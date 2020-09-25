import allure
import requests

@allure.feature("请求URL")
@allure.story("请求百度网址")
@allure.title("用例1")
def test_get_url():
    r = requests.get("https://wwww.baidu.com/")
    r1 = requests.get("https://wwww.baidu.com/")
    sess = requests.sessions()
    r3 = sess.request(method="GET", url="https://wwww.baidu.com/")
    print(r.text)
    print(r1.text)
    print(r3.text)
    pass


@allure.feature("用户模块")
@allure.story("查询用户")
@allure.title("用例2")
def test_get_params():
    params = {"accountName": "wuxian9617"}
    r = requests.request("GET", "http://qa.yansl.com:8084/acc/getBills", params=params)
    print(r.text)

@allure.feature("产品模块")
@allure.story("查询产品")
@allure.title("用例3")
def test_get_path(pub_data):
    dict= []
    headers ={"token":pub_data["token"]}
    r = requests.request("GET","http://qa.yansl.com:8084/product/getAllProd/{pageNum}/{pageSize}".format(pageNum="1",pageSize="40"),headers=headers)
    print(r.text)
    # r2 = r['data']['productCode']
    # print(r2.text)

@allure.feature("产品模块")
@allure.story("下载文件")
@allure.title("用例4")
def test_get_files(pub_data):
    with allure.step("第一步，准备测试数据"):pass
    file = {"pridCode":"1000"}
    headers = {"token": pub_data["token"]}
    with allure.step("第二步，发送请求"):pass
    r = requests.request("GET","http://qa.yansl.com:8084/product/downProdRepertory",params=file,headers=headers)
    with allure.step("第三部，请求数据"):
        allure.attach("请求行，请求头，请求正文",allure.attachment_type.TEXT)
    with open("test.xls","wb")  as f:
        f.write(r.content)





