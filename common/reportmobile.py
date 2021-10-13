import os
import shutil
import time
from pathlib import Path, PureWindowsPath

import self

from config import read_data_config


# 当前路径下指定的reportfile文件或目录是否存在存在
# if not os.path.exists("reportfile"):
#     os.mkdir("reportfile")
#     print("reportfile目录不存在：" + "reportfile")
# else:
#     print("reportfile目录存在：" + "reportfile")
# now = time.strftime("%Y_%m_%d_%H_%M_%S")
# print("当前时间" + now)
class repotmob:
    def remobile(self):
        # 获取data_name
        data_name = read_data_config.data_name
        # 获取当前py文件绝对路径
        cur_path = os.path.dirname(os.path.realpath(__file__))
        # 获取当前py文件上层目录
        up_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # file_namedata复制文件路径
        file_namedata = os.path.join(up_path, "report") +"/"+ data_name
        print("report复制文件路径:"+file_namedata)
        my_filedata = Path(file_namedata)
        # 需要操作log目录
        file_namelog = os.path.join(up_path, "logs") + "/" + data_name
        my_filelog = Path(file_namelog)
        print("logs复制文件路径:" + file_namelog)

        # 判断report是否存在data_name目录
        if not my_filedata.exists():
            print("report下目录：【%s" % data_name+"】目录不存在，创建一个")
            os.path.join(up_path, "report")
            os.mkdir(file_namedata)
        else:
            print("report下目录：【%s" % data_name+"】目录存在")
        # 移动文件report
        repotmob.filemove(self, data_name, up_path, 'report', '.html')
        # logs 判断logs是否存在data_name目录
        if not my_filelog.exists():
            print("logs目录：【%s" % data_name+"】目录不存在，创建一个")
            os.mkdir(file_namelog)
        else:
            print("logs目录：【%s" % data_name+"】目录存在")
        # 移动文件logs
        repotmob.filemove(self, data_name, up_path, 'logs', '.log')

    '''
        data_name:名称
        up_path：上层路径
        directory：/操作目录 report/logs
        namesuffix:文件后缀（.logs  .html)
    '''
    def filemove(self, data_name, up_path, directory, namesuffix):
        path_on_windows = PureWindowsPath(up_path)  # 转化成反斜杠
        # mypath = os.path.join(up_path, "report")  # 连接路径
        mypath = os.path.join(up_path, directory)  # 连接路径复制路径
        file_namedata = os.path.join(mypath, data_name) #复制后路径
        print("当前移动目录路径：" + mypath)
        print("当前移动目录路径：" + mypath)
        filelist = os.listdir(mypath)  # 返回mypath目录下的文件、文件夹
        print("1:" + str(filelist))
        i = 0
        j = 0
        for files in filelist:
            i += 1
            # print(os.path.splitext(files))
            # print("目录：【{}】,下第【{}】文件名称：{}".format(mypath, i, files))
            filenameone = os.path.splitext(files)[1]  # 读取文件后缀名
            filenametwo = os.path.splitext(files)[0]  # 读取文件名
            m = filenameone == namesuffix
            print("第【{}】个文件后缀是否为{}：{}；【{}】".format(i, namesuffix, m, filenameone))
            mm = data_name in filenametwo
            print("第【{}】个文件名称是否包含：【{}】,：{}".format(i, data_name, mm))
            if m and mm:
                j += 1
                print("文件名称包含：【{}】,后缀为：{}".format(data_name, namesuffix))
                full_path = os.path.join(mypath, files)  # 连接两个或更多的路径名组件
                print("复制文件：【%s" % full_path + "】")
                despath = os.path.join(file_namedata, files)  # .jpg为你的文件类型，即后缀名，读者自行修改
                print("复制后文件：【%s" % despath + "】")
                """
                        # filelist
                        # full_path 需要复制、移动的文件
                        # dstpath 目的地址
                        # shutil.move(full_path, dstpath)
                """
                shutil.move(full_path, despath)
                print("文件夹：【{}】,文件：【{}】移动成功".format(mypath, files))
            else:
                continue
        print("目录：【{}】,共有：【{}】个文件、文件夹；符合条件的有【{}】个".format(mypath, i, j))

if __name__ == '__main__':
    repotmob.remobile(self)