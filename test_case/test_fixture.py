import pytest

# 只要被pytest.fixture()装饰器修饰的函数就是fixture函数
# @pytest.fixture()
# def aa():
#     return 11
#
#
# def test_aa(aa):
#     print(aa)




'''
socpe表示作用域范围，从小到大
function ：每个用例被运行之前会被执行一次
class ：每个类被运行之前会被执行一次
module ：每个模块被运行之前会被执行一次
session ：项目启动时会被运行一次
'''

@pytest.fixture(scope="class") # 作用域
def aa():
    print("fixture函数被运行了")
    return 11

class Test111():
    def test_aa(self,aa):
        print(aa)
    def test_bb(self,aa):
        print(aa)

class Test222():
    def test_aa(self,aa):
        print(aa)
    def test_bb(self,aa):
        print(aa)