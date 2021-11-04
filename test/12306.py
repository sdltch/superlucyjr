"""
------------------------------------
@Time : 2021/10/21 14:07
@Auth : DALONG
@File : 12306.PY
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 5962@qq.com
@GROUP: 5962
------------------------------------
"""

# tornado框架搭建一个http服务器
from tornado import web
from tornado import httpserver
from tornado import ioloop

# 逻辑处理模块
class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello world')

# 逻辑处理模块 登录
class loginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('hello world')
        self.render('login.html')
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if username == 'admin' and password == '123456':
            self.write("登录成功！")
            print(username,password)
        else:
            self.write("账号或者密码错误！")
            print(username, password)
# 逻辑处理模块 img
class ImgHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('hello world')
        # 获取图片二进制信息
        with open('11.png', 'rb') as f:
            img_data=f.read()
            self.write(img_data)
            self.set_header("Content-Type", "image/png")


# 路由
application = web.Application([
        (r"/",IndexHandler),
        (r"/index",IndexHandler),
        (r"/login",loginHandler),
        (r"/img",ImgHandler),
    ])

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()