import pytest
import json
import requests
from common.commonData import CommonData
class HttpUtil():
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':'application/json;charset=UTF-8'}
    def post(self,path,data):
        host=CommonData.host
        data_json=json.dumps(data)
        if CommonData.token is not None:
            self.headers['token']=CommonData.token
        req_login=self.http.post(url=host+path,proxies=CommonData.proxies,
                          data=data_json,headers=self.headers)
        assert req_login.status_code == 200
        req_json=req_login.text
        req_dict=json.loads(req_json)
        return  req_dict
# assert  req.status_code==200
# req_token=json.loads(req.text)
# token=req_token["object"]['token']
# headers['token']=token
# data={'token':token}
# data_json=json.dumps(data)
# req=http.post("http://192.168.1.203:8083/sys/getUserInfo",proxies=proxies,
#                   data=data_json,headers=headers)
# print(req.content.decode())
# req=requests.post("http://192.168.1.203:8083/sys/logout")

# print(req.text)
# print(req.headers)
# print(req.content.decode())
# print(req.cookies)
# print(req.status_code)
# print(req.apparent_encoding)
# print(req.request)
# print(req.history)
# print(req.encoding)
# print(req.links)
# print(req.next)
# print('http code',req.status_code)
