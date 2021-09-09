import os
import time

import self


class repotmob:
    def remobile(self):
        # 获取当前py文件绝对路径
        cur_path = os.path.dirname(os.path.realpath(__file__))
        print("当前路径"+cur_path)
        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        print("当前时间" + now)
        if not os.path.exists("reportfile"):
            os.mkdir("reportfile")
            print("目录不存在" + "reportfile")
        else:
            print("目录存在" + "reportfile")
        # 测试报告路径
        file_name = os.path.join(cur_path, "report") + "/" + now + "-report.html"

if __name__ == '__main__':
    repotmob.remobile(self)