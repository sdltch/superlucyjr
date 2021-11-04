"""
------------------------------------
@Time : 2021/10/21 17:22
@Auth : DALONG
@File : requesthead.PY
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 5962@qq.com
@GROUP: 5962
------------------------------------
"""
import re
"""
转化json格式
"""

headers_str = '''
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive

'''
pattern = '^(.*?): (.*)$'

for line in headers_str.splitlines():
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))