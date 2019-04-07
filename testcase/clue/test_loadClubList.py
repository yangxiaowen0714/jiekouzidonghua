from common.commonData import CommonData
from conftest import http
import allure
class Test_LoadClueList:
    def test_LoadClueList(self):
        path="/clue/loadClueList"
        data={'token':CommonData.token}
        res_getuserinfo=http.post(path,data)
        assert res_getuserinfo['code']==200
        assert  res_getuserinfo['msg']=="操作成功"