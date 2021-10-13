import logging
import time
import os

from config import read_data_config


class MyLogging:

    def __init__(self):
        # 获取data_name
        data_name = read_data_config.data_name
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        print(timestr)
        lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../logs'))
        print(lib_path)
        filename = lib_path + '/' + timestr +"_"+ data_name + '.log'  # 日志文件的地址
        self.logger = logging.getLogger()  # 定义对应的程序模块名name，默认为root
        self.logger.setLevel(logging.INFO)  # 必须设置，这里如果不显示设置，默认过滤掉warning之前的所有级别的信息

        sh = logging.StreamHandler()  # 日志输出到屏幕控制台
        sh.setLevel(logging.INFO)  # 设置日志等级

        fh = logging.FileHandler(filename=filename, encoding='utf-8')  # 向文件filename输出日志信息
        fh.setLevel(logging.INFO)  # 设置日志等级

        # 设置格式对象
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s")  # 定义日志输出格式

        # 设置handler的格式对象
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 将handler增加到logger中
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)


if __name__ == "__main__":
    MyLogging
    log = MyLogging().logger
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.critical("critical")
