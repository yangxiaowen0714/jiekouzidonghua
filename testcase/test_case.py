# import pytest
# @pytest.fixture()
# def my_fixture():
#     print("初始化操作")
#     yield
#     print("数据恢复")
# class Test():
#     @pytest.mark.usefixtures("my_fixture")
#     def test_first(self):
#         pass
#     # assert 1==2
# #     @pytest.mark.debug
#     def test_two(self):
#         print("第er个")
# #     # assert 1==1
# def test_three():
#     print("第三个")
#     str1='qwe'
#     str2='qwert'
#     # assert str1 in str2
# def test_four():
#     print("第四个")
#     b=[1,2,3,5,9]
#     # assert  8 in b
# def test_five():
#     print("第五个")
#     # assert True
# def test_six():
#     print("第六个")
#     a=[1,2]
#     b=[1,2]
    # assert a!=b
#
# if __name__ == '__main__':
#         pytest.main("-s")#标准输出