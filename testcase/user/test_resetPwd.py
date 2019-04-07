from common.commonData import CommonData
from conftest import http
class Test_ResetPwd:
    def test_ResetPwd(self):
        path="/user/resetPwd"
        data={'token':CommonData.token,'id':1}
        res_getuserinfo=http.post(path,data)
        assert res_getuserinfo['code']==200
        assert  res_getuserinfo['msg']=="操作成功"