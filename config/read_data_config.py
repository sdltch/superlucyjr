# coding:utf-8
import os
import configparser
# data
# os.path.realpath(__file__)：返回当前文件的绝对路径
# os.path.dirname()： 返回（）所在目录
cur_path = os.path.dirname(os.path.realpath(__file__))  # 当前文件的所在目录
configPath = os.path.join(cur_path, "data_config.ini")  # 路径拼接：/config/email_config.ini
conf = configparser.ConfigParser()
conf.read(configPath, encoding='UTF-8')  # 读取/config/data_config.ini 的内容

# get(section,option) 得到data_name的值，返回为string类型
data_name = conf.get("data", "data_name")

