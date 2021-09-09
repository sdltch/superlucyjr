import os
import shutil
import time
from pathlib import Path

import self

from config import read_data_config


class repotmob:
    def remobile(self):
        # 获取data_name
        data_name = read_data_config.data_name
        # 获取当前py文件绝对路径
        cur_path = os.path.dirname(os.path.realpath(__file__))
        # 获取当前py文件上层目录
        up_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # 需要操作目录
        # file_name = os.path.join(up_path, "report")+"\winreport"
        file_name = os.path.join(up_path, "report") +"/"+ data_name
        my_file = Path(file_name)
        print("当前操作目录:" + file_name)
        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        print("当前时间" + now)
        if not my_file.exists():
            print("目录：%s" % data_name+"不存在，创建一个")
            os.mkdir("../report/"+data_name)
        else:
            print("目录：%s" % data_name+"存在")

        # srcfile 需要复制、移动的文件
        # dstpath 目的地址

        # shutil.move(srcfile, dstpath + fname)
        # 指定的文件或目录存在
        if not os.path.exists("reportfile"):
            # os.mkdir("reportfile")
            print("目录不存在" + "reportfile")
        else:
            print("目录存在" + "reportfile")
        # 测试报告路径
        print("sadfa"+os.path.join(cur_path, "report"))
        file_name = os.path.join(cur_path, "report") + "/" + now + "-report.html"

if __name__ == '__main__':
    repotmob.remobile(self)