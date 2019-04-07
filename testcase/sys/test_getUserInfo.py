from common.commonData import CommonData
from conftest import http
import allure
@allure.feature("登录相关接口")
class Test_GetUserInfo:
    @allure.story("请求获取用户信息")
    def test_GetUserInfo(self):
        path="/sys/getUserInfo"
        data={'token':CommonData.token}
        res_getuserinfo=http.post(path,data)
        assert res_getuserinfo['code']==200