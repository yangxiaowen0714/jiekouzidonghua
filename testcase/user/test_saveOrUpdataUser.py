from common.commonData import CommonData
from conftest import http
class Test_SaveOrUpdataUser:
    def test_SaveOrUpdataUser(self):
        path="/user/saveOrUpdateUser"
        data={'token':CommonData.token,
              "nickName": "978415",
              "userName": "15895458655",
              "telNo": "",
              "email": "",
              "address": ""}
        res_getuserinfo=http.post(path,data)
        assert res_getuserinfo['code']==412