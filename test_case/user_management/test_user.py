import random

from tools.api import request_tool
import pytest
from tools.data import excel_tool

def test_userlogin(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
      "pwd": "wsx666666",
      "userName": "wsx6666"
    }
    '''
    status_code = 200  # 响应状态码
    expect = "登录成功"  # 预期结果
    json_path = [{"token": "$['data]['token]"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(json_path=json_path, method=method, url=uri, pub_data=pub_data, json_data=json_data,
                         status_code=status_code, expect=expect, feature=feature, story=story, title=title)


def test_userlock(pub_data):
    # print(headers)
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '冻结用户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/lock"  # 接口地址
    params = {"userName": "wuxian4139"}
    headers = {"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    request_tool.request(method=method, url=uri, pub_data=pub_data, params=params, status_code=status_code,
                         expect=expect, headers=headers, feature=feature, story=story, title=title)


def test_unLock(pub_data):
    # print(headers)
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '冻结用户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/unLock"  # 接口地址
    params = {"userName": "wuxian4139"}
    headers = {'token': '${token}'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    request_tool.request(method=method, url=uri, pub_data=pub_data, params=params, status_code=status_code,
                         expect=expect,
                         headers=headers, feature=feature, story=story, title=title)


def test_get_queryuser(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/getCustomer"  # 接口地址
    params = {"phone": "15097858616"}
    headers = {'token': '${token}'}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    request_tool.request(method=method, url=uri, pub_data=pub_data, params=params, status_code=status_code,
                         expect=expect, headers=headers, feature=feature, story=story, title=title)


def test_get_alluser(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询所有用户'  # allure报告中二级分类
    title = "查询所有用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/getAll/{}/{}".format(1, 20)  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = None
    headers = {"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, params=params, status_code=status_code,
                         expect=expect, feature=feature, story=story, title=title, headers=headers)


def test_get_file(pub_data, db):
    file_name = "test.xlsx"  # 下载文件地址
    method = "GET"  # 请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '下载库存信息'  # allure报告中二级分类
    title = "下载库存信息_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/downProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    res = db.select_execute("select product_code from t_prod_product;")
    params = {"pridCode": random.choices(res)[0]}
    headers = {"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, params=params, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title, headers=headers)
    with open(file_name, "wb") as f:
        f.write(r.content)


# def test_post_file(pub_data):
#     file_name = "/Users/weishixing/PycharmProjects/apitest/test_case/user_management/test.xls" # 上传文件地址
#     method = "POST"  #请求方法，全部大写
#     feature = "库存模块"  # allure报告中一级分类
#     story = '盘点库存'  # allure报告中二级分类
#     title = "盘点库存"  # allure报告中用例名字
#     uri = "/product/uploaProdRepertory"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     files = {"file":open(file_name,'rb')}
#     headers={"token":"${token}"}
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,files=files,status_code=status_code,expect=expect,
#                          feature=feature,story=story,title=title,headers=headers)



#
# data = excel_tool.get_test_case("test.xlsx")
# @pytest.mark.parametrize("account_name,money,expect", data[1], ids=data[0])
# def test_charge(pub_data, account_name, money, expect):
#     pub_data['account_name'] = account_name
#     pub_data['money'] = money
#     method = "POST"  # 请求方法，全部大写
#     feature = "账户模块"  # allure报告中一级分类
#     story = '充值'  # allure报告中二级分类
#     title = None  # allure报告中用例名字
#     uri = "/acc/recharge"  # 接口地址
#     headers = {"token": "${token}"}
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
#     {
#       "accountName": "${account_name}",
#       "changeMoney": "${money}"
#     }
#     '''
#     status_code = 200  # 响应状态码
#     expect = expect  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data,
#                          status_code=status_code, expect=expect, headers=headers, feature=feature, story=story,
#                          title=title)

@pytest.mark.mockes
def test_changeBalance(pub_data):
    pub_data['number']="自动生成 数字 100,1000"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '修改账户余额'  # allure报告中二级分类
    title = None  # allure报告中用例名字
    uri = "/acc/changeBalance/{}".format(17344)  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
     {
      "balance": "${number}"
    }
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,
                         status_code=status_code,expect=expect,feature=feature,story=story,title=title)

@pytest.mark.mockes
def test_user_charge(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '扣款'  # allure报告中二级分类
    title = None  # allure报告中用例名字
    uri = "/acc/charge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
      "accountName": "wuxian9617",
      "changeMoney": "自动生成 数字 1,100"
    }
    '''
    status_code = 200  # 响应状态码
    expect = "扣款成功"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,
                         expect=expect,feature=feature,story=story,title=title)


def test_post_flow(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"accountName":"wuxian9617"}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,
                         expect=expect,feature=feature,story=story,title=title)
