from common.commonData import CommonData
from conftest import http
import allure
@allure.feature("区划相关接口")
class Test_LoadAttachData:
    @allure.story("场所信息归属地初始化数据")
    def test_LoadAttachData(self):
        path="/region/loadAttachData"
        data={'token':CommonData.token}
        res_getuserinfo=http.post(path,data)
        assert res_getuserinfo['code']==200
        assert  res_getuserinfo['msg']=="操作成功"