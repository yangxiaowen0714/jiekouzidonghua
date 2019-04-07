from common.commonData import CommonData
from conftest import http
import allure
@allure.feature("用户相关接口")
class Test_LoadUserInfo:
    @allure.story("请求获取用户列表")
    def test_LoadUserInfo(self):
        path="/user/loadUserInfo"
        data={'token':CommonData.token,'id':724}
        res_getuserinfo=http.post(path,data)
        assert res_getuserinfo['code']==200
        assert  res_getuserinfo['msg']=="操作成功"