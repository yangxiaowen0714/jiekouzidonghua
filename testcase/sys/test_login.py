# from common.commonData import CommonData
# from conftest import http
# class Test_Login:
#     def test_login(self):
#         path="/sys/login"
#         data = {'userName': '15935158361', 'password': '123456'}
#         res_getuserinfo=http.post(path,data)
#         assert res_getuserinfo['code']==200
#         assert  res_getuserinfo['msg']=="操作成功"
#         assert  res_getuserinfo['object']['userId']==164
#     def test_fail_login_password(self):#密码错误
#         path="/sys/login"
#         data = {'userName': '15935158361', 'password': '123456789'}
#         res_getuserinfo=http.post(path,data)
#         assert res_getuserinfo['code']==410
#         assert res_getuserinfo['msg'] == "用户名或密码错误"
#     def test_fail_login_username(self):#用户名为空
#         path="/sys/login"
#         data = {'userName': '', 'password': '123456'}
#         res_getuserinfo=http.post(path,data)
#         assert res_getuserinfo['code']==3010
#         assert res_getuserinfo['msg'] == "此账户禁止登录"
#     def test_fail_login_username_no(self):#用户名不存在                               有问题
#         path="/sys/login"
#         data = {'userName': '159351583618', 'password': '123456'}
#         res_getuserinfo=http.post(path,data)
#         assert res_getuserinfo['code']==301
#         assert res_getuserinfo['msg'] == "用户不存在"