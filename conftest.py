from util.httpUtil import HttpUtil
import  pytest
from common.commonData import CommonData
http=HttpUtil()
@pytest.fixture(scope='session',autouse=True)
#session/module/class/function
def login():
    path="/sys/login"
    data={'userName':'15935158361','password':'123456'}
    req_login = http.post(path,data)
    CommonData.token=req_login['object']['token']
    print("登录成功")
    yield
    path="/sys/logout"
    data = {'token': CommonData.token}
    res_logout = http.post(path, data)
    assert res_logout['code'] == 200
    print("退出成功")
