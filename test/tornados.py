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
    def get(self, *args,**kwargs):
        self.write('hello world')

# 路由
application = web.Application([
        (r"/",IndexHandler),
    ])

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()