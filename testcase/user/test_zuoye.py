# from common.commonData import CommonData
# from conftest import http
# import random
# class Test_SaveOrUpdataUser:
#     def test_SaveOrUpdataUser(self):
#         nickname=str(random.randint(10000000,100000000))
#         mobile='159'+nickname
#         path="/user/saveOrUpdateUser"
#         data={'token':CommonData.token,
#               "nickName": nickname,
#               "userName": mobile,
#               "telNo": "",
#               "email": "",
#               "address": ""}
#         res_getuserinfo=http.post(path,data)
#         assert res_getuserinfo['code']==401
#         path = "/sys/login"
#         data = {'userName':mobile, 'password': '123456'}
#         res_getuserinfo=http.post(path,data)
#         print(res_getuserinfo['object']['userId'])
#     def test_LoadUserList(self):
#         path="/user/loadUserList"
#         data={'token':CommonData.token}
#         res_getuserinfo=http.post(path,data)
#         assert res_getuserinfo['code']==200
#         assert  res_getuserinfo['msg']=="操作成功"
#         print(res_getuserinfo['object']['list'][0]['id'])
