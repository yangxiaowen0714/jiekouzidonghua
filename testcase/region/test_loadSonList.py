from common.commonData import CommonData
from conftest import http
import allure
@allure.feature("区划相关接口")
class Test_LoadSonList:
    @allure.story("查询当前节点下的子节点")
    def test_LoadSonList(self):
        path="/region/loadSonList"
        data={'token':CommonData.token,'id':100}
        res_getuserinfo=http.post(path,data)
        assert res_getuserinfo['code']==200
        assert  res_getuserinfo['msg']=="操作成功"