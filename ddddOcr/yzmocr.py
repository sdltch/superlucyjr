"""
------------------------------------
@Time : 2021/10/28 9:08
@Auth : DALONG
@File : yzmocr.PY
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 5962@qq.com
@GROUP: 5962
# pip install ddddocr -i https://pypi.tuna.tsinghua.edu.cn/simple
------------------------------------
"""
import base64
import itertools
import os
import itertools as itr
import re

import ddddocr
from common.send_request import RunMethod


# ddddocr识别验证码


def amipngocr(test_img_pathone):
    ocrone = ddddocr.DdddOcr()
    # # 传入的test_img_pathone为图片路径，需要转化
    # with open(test_img_pathone, 'rb') as f:
    #     test_img_pathone = f.read()
    # 传入的test_img_pathone为base64图片解码后值
    res = ocrone.classification(test_img_pathone)
    print("验证码:{}".format(res))
    ocr= ocrManage(res)
    print("验证码处理结果:{}".format(ocr))
    return str(ocr)
# 判断识别后验证码
def ocrManage(myres):
    take = ['x', '*']
    addition = ['/', '7', '1', '(']
    add = ['+', '4']
    Reduction = ['-']
    for i in take:
        if i == myres[1]:
            print("验证码乘法处理: {}".format(myres[1]))
            # myresult = myres.split('x')
            try:
                ocrresult = int(myres[0]) * int(myres[2])
                print("验证码计算结果: {} * {} = {}".format(myres[0], myres[2], int(ocrresult)))
                return int(ocrresult)
            except:
                print("验证码异常:{}".format(myres))
    for j in addition:
        if j == myres[1]:
            print("验证码除法处理{}".format(myres[1]))
            try:
                ocrresult = int(myres[0]) / int(myres[2])
                print("验证码计算结果: {} / {} = {}".format(myres[0], myres[2], int(ocrresult)))
                return int(ocrresult)
            except:
                print("验证码异常:{}".format(myres))
    for k in add:
        if k == myres[1]:
            print("验证码加法处理{}".format(myres[1]))
            try:
                ocrresult = int(myres[0]) + int(myres[2])
                print("验证码计算结果: {} + {} = {}".format(myres[0], myres[2], int(ocrresult)))
                return int(ocrresult)
            except:
                print("验证码异常:{}".format(myres))
    for l in Reduction:
        if l == myres[1]:
            print("验证码减法处理{}".format(myres[1]))
            try:
                ocrresult = int(myres[0]) - int(myres[2])
                print("验证码计算结果: {} - {} = {}".format(myres[0], myres[2], int(ocrresult)))
                return int(ocrresult)
            except:
                print("验证码异常:{}".format(myres))

def mybase(imgurl):
    "base64图片解码，保存图片"
    # base64
    codeurl = base64.b64decode(imgurl)
    # print("base64 :{}".format(codeurl))
    return codeurl

def get_image(codeurl):
    "base64图片解码，保存图片"
    # imgurlone = imgurl[0]
    # base64
    # codeurl = base64.b64decode(imgurlone)
    # print("base64 :{}".format(codeurl))
    # 1
    # 获取当前py文件绝对路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    # 获取当前py文件上层目录
    up_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # 转化斜杠
    linux_path = up_path.replace('\\', '/')
    test_img_pathone = linux_path+'/ddddOcr/imgpng/code7.png'
    with open(test_img_pathone, 'wb') as f:
        f.write(codeurl)
    # 2
    # f = open('code.png', 'wb')
    # f.write(codeurl)
    f.close()

def violence(password,MaxLenPassword):
    # 密码字符集合
    # words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+|">?:'
    words = 'sdl123@'
    # MaxLenPassword = 6   # 最大密码长度
    wordList="sdl@123"  #
    reg = "\\$\\{[a-zA-Z0-9]+\\}"  # 定义正则表达式
    for lenPassword in range(1, MaxLenPassword + 1):
        # passWd = itertools.product(wordList, repeat =lenPassword)  # 调用迭代函数 自匹配
        passWd = itr.product(wordList, repeat =lenPassword)
        dic = open('imgpng/pass.txt','w')
        passgood = open('imgpng/password.txt', 'w')
        for i in passWd:
            newstr = ''.join(i)
            print("每次登录密码为:{};类型{}".format(newstr,type(newstr)))
            url = 'http://apis.develop.customs.dev.amiintellect.com/api/connect/auth/authorize'
            # data = 'password=${pass}&username=sdltest&grant_type=password'
            data = {
                    "loginName": "sdl001",
                    "password": "123456",
                    "returnUrl": "/home"
                    }
            parmsType = "json"
            files = None
            myheader = {}
            # 处理headers
            myheader["Authorization"] = "Basic c3VwZXJsdWN5X3N5bmVyZ3k6c3luZXJneS0xcWF6LTJ3c3g="
            r = RunMethod()
            if 'from' == parmsType:
                print('处理from')
                mypasslist = re.findall(reg, data)
                if mypasslist:
                    print("mypasslist：{}".format(mypasslist))
                    data = data.replace(mypasslist[0], newstr)
            if 'json' == parmsType:
                print('处理json')
                data["password"] = newstr
            # print("mypasslist：{} ,data ：{}".format(mypasslist, data))
            newuser = data["loginName"]
            res = r.do_post(url, data, parmsType, myheader, files)
            newres = str(res)
            print("返回结果：{},返回类型：{}".format(res, type(str(res))))
            dic.write("密码:"+newstr+";")
            if '错误' in newres:
                print("登录成功: 账号: {}; 密码: {}".format('sdltest',newstr))
                passgood.write("账号："+newuser+"；密码:"+newstr)
                break
            else:
                print("登录失败,继续登录")
        dic.close()
        passgood.close()

if __name__ == '__main__':
    ''' 1 test_img_pathone:路径处理'''
    # # 获取当前py文件绝对路径
    # cur_path = os.path.dirname(os.path.realpath(__file__))
    # # 获取当前py文件上层目录
    # up_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # # 转化斜杠
    # linux_path = cur_path.replace('\\', '/')
    # print("路径:{}".format(cur_path))
    # test_img_pathone = cur_path +'imgpng/code.png'

    ''' 2 test_img_pathone:base处理'''

    imgurl = "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"
    imgurl = "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"
    imgurl = "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"
    imgurl = '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'
    # imgurl = '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'
    imgurl = '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'
    test_img_pathone = mybase(imgurl)

    get_image(test_img_pathone)
    amipngocr(test_img_pathone)
    # 密码破解
    # violence('2',1)
