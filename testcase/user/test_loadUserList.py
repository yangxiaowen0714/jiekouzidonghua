from common.commonData import CommonData
from conftest import http
class Test_LoadUserList:
    def test_LoadUserList(self):
        path="/user/loadUserList"
        data={'token':CommonData.token}
        res_getuserinfo=http.post(path,data)
        assert res_getuserinfo['code']==200
        assert  res_getuserinfo['msg']=="操作成功"