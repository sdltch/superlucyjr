import ast
import json
from pathlib import PureWindowsPath, Path

import requests
import re

# from common.logger import MyLogging
# log = MyLogging().logger

# #使用python代码发送https请求
# import requests
# requests.packages.urllib3.disable_warnings()#忽略警告
# def login(inData):
#     url="https://www.imooc.com/passport/user/prelogin"
#     payload = inData
#     resp = requests.post(url,data=payload,verify = False)#verify = False关闭认证
#     print(resp.text)
# login({"username":"tiger","password":"123456"})



requests.packages.urllib3.disable_warnings()#忽略警告
class RunMethod:
    # post请求
    requests.packages.urllib3.disable_warnings()  # 忽略警告
    def do_post(self, url, data, parmsType, headers=None, filepath=None):
        res = None
        if parmsType == 'json' or parmsType == 'JSON':
            # log.info("最终parmsType = {}".format(parmsType))
            if headers != None:
                if filepath != None:
                    res = requests.post(url=url, json=data, files=filepath, headers=headers, verify = False)
                else:
                    res = requests.post(url=url, json=data, headers=headers, verify = False)
            else:
                if filepath != None:
                    res = requests.post(url=url, json=data, files=filepath, verify = False)
                else:
                    res = requests.post(url=url, json=data, verify = False)
        else:
            # log.info("最终parmsType = {}".format(parmsType))
            if headers != None :
                if filepath != None:
                    res = requests.post(url=url, data=data, files=filepath, headers=headers, verify = False)
                else:
                    res = requests.post(url=url, data=data, headers=headers, verify = False)
            else:
                if filepath != None:
                    res = requests.post(url=url, data=data, files=filepath, verify = False)
                else:
                    res = requests.post(url=url, data=data, verify = False)
        print("res:"+str(res))
        return res.json()

    #
    requests.packages.urllib3.disable_warnings()  # 忽略警告
    def do_get(self, url, data=None, headers=None):
        res = None
        if headers != None:
            res = requests.get(url=url, data=data, headers=headers, verify = False)
        else:
            res = requests.get(url=url, data=data, verify = False)
        return res.json()

    # put请求
    requests.packages.urllib3.disable_warnings()  # 忽略警告
    def do_put(self, url, data=None, headers=None):
        res = None
        if headers != None:
            res = requests.put(url=url,json=data,headers=headers, verify = False)
        else:
            res = requests.put(url=url, json=data, verify = False)
        return res.json()

    # delete请求
    requests.packages.urllib3.disable_warnings()  # 忽略警告
    def do_delete(self, url, data, headers=None):
        res = None
        if headers != None:
            res = requests.delete(url=url,data=data,headers=headers, verify = False)
        else:
            res = requests.delete(url=url,data=data, verify = False)
        return res.json()

    def run_method(self, method, parmsType, url, data, headers, myami, filepath):
        myheader={}
        # 处理headers
        if len(headers) == 0:
            print("headers为空")
            if "tokenHeads" in myami and "tokenone" in myami:
                myheader["Authorization"] = myami["tokenHeads"]+myami["tokenone"]
            else:
                print("headers取不到Authorization")
        else:
            print("headers不为空")
            if headers == 'no' or headers =='NO':
                print("headers为no/NO不处理")
            else:
                print("headers不为no")
                if "tokenHeads" in myami and "tokenone" in myami:
                    myheader["Authorization"] = myami["tokenHeads"] + myami["tokenone"]
                else:
                    print("headers取不到Authorization")
                if '&' in headers:
                    print("headers包含为&")
                    splitone = headers.split("&")
                    for i in splitone:
                        # :号处理
                        if ':' in i:
                            splittwo = i.split(":")
                            print("value:" + splittwo[1])
                            ss = RunMethod.myvariable(self, splittwo[1], myami)
                            myheader[splittwo[0]] = ss
                else:
                    # =号处理
                    print("headers不包含为&")
                    if ':' in headers:
                        splittwo = headers.split(":")
                        print("value:" + splittwo[1])
                        ss = RunMethod.myvariable(self, splittwo[1], myami)
                        myheader[splittwo[0]] = ss

        # 根据入参类型给的Content-Type
        # log.info("data数据类型1:" + str(type(data)))
        if parmsType=='json' or parmsType=='JSON':
            myheader['Content-Type']  = "application/json;charset=UTF-8"
            data = json.loads(data)  # 字典对象转换为json字符串
        elif parmsType=='from' or parmsType=='FROM':
            myheader['Content-Type'] = "application/x-www-form-urlencoded;charset=UTF-8"
        elif parmsType=='fromdata' or parmsType=='FROMDATA':
            data = ast.literal_eval(data)  # 转化成字典
            myheader['Content-Type'] = "application/x-www-form-urlencoded;charset=UTF-8"
        elif parmsType == 'fromsend' or parmsType == 'FROMSEND':
            data = ast.literal_eval(data)  # 转化成字典
            # boundary = "------WebKitFormBoundaryerEzPLp0xMCUtCXe";
            # myheader['Content-Type'] = "multipart/form-data; boundary="+boundary
            # myheader['Content-Type'] = "multipart/form-data;boundary=------WebKitFormBoundaryerEzPLp0xMCUtCXe"

        # log.info("data数据类型2:"+ str(type(data)))

        # for i in myheader:
            # log.info("最终header：%s" % myheader)
        files = None
        # filepath不为空处理文件
        if len(filepath) != 0:
            # log.info("最终filepath：{},不为空".format(filepath))
            # binary上传文件
            files = {"file": open("E:/amisrobot/amisbook识别文件/ami微服务/报关单/发票.xls", "rb")}
            # files = {'file': open(filepath, 'rb').read()}
        # else:
            # log.info("最终filepath：{},为空".format(filepath))

        if method == "POST" or method == "post":
            res = self.do_post(url, data, parmsType, myheader, files)
        elif method  == "GET" or method == "get":
            res = self.do_get(url, data, myheader)
        elif method == "PUT" or method == "put":
            res = self.do_put(url, data, myheader)
        elif method == "DELETE" or method == "delete":
            res = self.do_delete(url, data, myheader)
        else:
          print("系统暂不支持该请求："+method)
        return res

    def myvariable(self, heads, myami):
        reg = "\\$\\{[a-zA-Z0-9]+\\}";  # 定义正则表达式
        regs = "[a-zA-Z0-9]+";  # 定义正则表达式
        n = heads
        # 是否包含=号
        if '$' in heads:
            print("包含$号:" + heads)
            # 正则提取
            nn = re.findall(regs, heads)
            nnn = nn[0]
            print("提取$后值为：:" + nnn)
            if nnn in myami:
                n = myami[nnn]
        else:
            print("不包含$号:" + heads)
        print("替换后值n为:" + n)
        return n

    def newgetdata(self, data, myami):
        reg = "\\$\\{[a-zA-Z0-9]+\\}";  # 定义正则表达式
        regs = "[a-zA-Z0-9]+";  # 定义正则表达式
        if '&' in data:
            # 正则提取
            nn = re.findall(reg, data)
            for i in nn:
                nnn=re.findall(regs, i)
                dataone=nnn[0]
                if dataone in myami:
                    data = data.replace(i,myami[dataone])
        print("更改后data:"+data)
        return data



if __name__ == '__main__':
    data ={
        "username": "0215测试001",
        "password": "123456",
        "returnUrl": "/home",
        "captchaId": "",
        "captchaCode": "undefined",
        "grant_type": "password"
    }
    url = 'http://v30.edge.customs.dev.amiintellect.com/api/auth/oauth/token'
    print("url:"+url)
    method ='post'
    headerone ={}
    headerone['Authorization']='Basic YW1paW50ZWxsZWN0OmFtaWludGVsbGVjdC0xMjM0NTY='
    # headerone['Content-Type'] = "application/x-www-form-urlencoded"
    # headerone['Content-Type'] = "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
    for i in headerone:
        print("key：{}; value：{}".format(i, headerone[i]))
        print("header:" + i)
    # headerone = {'Authorizatio': 'Basic YW1paW50ZWxsZWN0OmFtaWludGVsbGVjdC0xMjM0NTY=',"Content-Type": "application/x-www-form-urlencoded"}
    re = requests.post(url=url, data=data, headers=headerone)
    # r = RunMethod()
    # print("111")
    #
    # re = r.do_post(url=url,data=data)
    print(re.json())
    #
    # res = requests.post(url=url, json=data,headers=headerone)
    # restwo = requests.post(url=url, json=data)
    # print(res)
    # print(res.json())
    # print(res.json()['data']['token'])
    # s= RunMethod()
    # ss = "id=${id}&names=${name}"
    # print("ss:"+ss)
    # dd ={}
    # dd["id"] ='asdf'
    # dd["name"] = 'AAAAAA'
    # s.newgetdata(ss,dd)


