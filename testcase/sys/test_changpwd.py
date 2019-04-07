# from common.commonData import CommonData
# from conftest import http
# import pytest
# class Test_ChangPwd:
#     # @pytest.mark.debug
#     # @pytest.mark.usefixtures("recoveryPwd")
#     def test_changpwd(self):
#         # newpwd="123456789"
#         path="/sys/changePwd"
#         data = {'userId':164,'userName': '15935158361', 'oldPwd':'123456789','password':'123456'}
#         res_getuserinfo=http.post(path,data)
#         assert res_getuserinfo['code'] == 200
#         assert res_getuserinfo['msg'] == "操作成功"
    # @pytest.mark.usefixtures("recoveryPwd")
    # def test_ChangPwd_success(self):
    #     newpwd=""
