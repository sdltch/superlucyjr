import ast
import json

import requests
import re

class RunMethod:
    # post请求
    def do_post(self, url, data, parmsType,headers=None):
        res = None
        if parmsType == 'json' or parmsType == 'JSON':
            if headers != None:
                res = requests.post(url=url, json=data, headers=headers)
            else:
                res = requests.post(url=url, json=data)
        else:
            print("formdata"+parmsType)
            if headers != None:
                res = requests.post(url=url, data=data, headers=headers)
            else:
                res = requests.post(url=url, data=data)
        print("res:"+str(res))
        return res.json()

    # get请求
    def do_get(self, url, data=None, headers=None):
        res = None
        if headers != None:
            res = requests.get(url=url, data=data, headers=headers)
        else:
            res = requests.get(url=url, data=data)
        return res.json()

    # put请求
    def do_put(self, url, data=None, headers=None):
        res = None
        if headers != None:
            res = requests.put(url=url,data=data,headers=headers)
        else:
            res = requests.put(url=url, data=data)
        return res.json()

    # delete请求
    def do_delete(self, url, headers=None):
        res = None
        if headers != None:
            res = requests.delete(url=url,headers=headers)
        else:
            res = requests.delete(url=url)
        return res.json()

    def run_method(self, method, parmsType, url, data, headers, myami):
        myheader={}
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
        if parmsType=='json' or parmsType=='JSON':
            myheader['Content-Type']  = "application/json;charset=UTF-8"
            data = json.loads(data)  # 字典对象转换为json字符串
        elif parmsType=='from' or parmsType=='FROM':
            myheader['Content-Type'] = "application/x-www-form-urlencoded;charset=UTF-8"
        elif parmsType=='fromdata' or parmsType=='FROMDATA':
            data = ast.literal_eval(data)  # 转化成字典
            myheader['Content-Type'] = "application/x-www-form-urlencoded;charset=UTF-8"
            # # 参数之间的分隔。随意设定，只要不会和其他的字符串重复即可。
            # boundary = "------WebKitFormBoundaryerEzPLp0xMCUtCXe";
            # myheader['Content-Type'] = "Content-Type","multipart/form-data; boundary="+boundary
            # multipart/form-data; boundary=----WebKitFormBoundarywlXH6Qc0vbvGjNGA
        for i in myheader:
            print("最终header："+i+":"+myheader[i])

        if method == "POST" or method == "post":
            res = self.do_post(url, data, parmsType, myheader)
        elif method  == "GET" or method == "get":
            res = self.do_get(url, data, myheader)
        elif method == "PUT" or method == "put":
            res = self.do_put(url, data, myheader)
        elif method == "DELTET" or method == "delete":
            res = self.do_delete(url, myheader)
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


