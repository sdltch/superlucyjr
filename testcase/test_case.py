import ast
import re

from common.operate_excel import *
import unittest
from parameterized import parameterized
from common.send_request import RunMethod
import json
from common.logger import MyLogging
import jsonpath
from common.is_instance import IsInstance
from HTMLTestRunner import HTMLTestRunner
import os
import time

from common.write_excel import mywrite


from config import read_data_config
# 获取data_name
data_name = str(read_data_config.data_name)
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data"))
# file_path = lib_path + "/" + "amirobotv30.xlsx"  # excel的地址
file_path = lib_path + "/" + data_name +".xlsx"  # excel的地址
sheet_name = "测试用例"
log = MyLogging().logger
myami = {}

def getExcelData():
    list = ExcelData(file_path, sheet_name).readExcel()
    return list

# UnitTest类必须继承Case类
class TestCase(unittest.TestCase):


    @parameterized.expand(getExcelData())
    def test_api(self, rowNumber, caseRowNumber, testCaseName, priority, apiName, url, method, parmsType, data,
                 checkPoint, myfile, response, headers, isRun, result ):
        isRun = isRun.upper();  # 转化成大写
        if isRun == "Y" or isRun == "y":
            log.info("【开始执行测试用例：{}】".format(caseRowNumber))
            # headers = {"Content-Type": "application/json"}
            # data = json.loads(data)  # 字典对象转换为json字符串
            c = checkPoint.split(",")
            log.info("用例设置检查点：%s" % c)
            print("用例设置检查点：%s" % c)
            log.info("请求rowNumber：%s" % rowNumber)
            log.info("请求caseRowNumber：%s" % caseRowNumber)
            log.info("请求testCaseName：%s" % testCaseName)
            log.info("请求priority：%s" % priority)
            log.info("请求apiName：%s" % apiName)
            log.info("请求url：%s" % url)
            method = method.upper();  # 转化成大写
            log.info("请求方法：%s" % method)
            parmsType = parmsType.upper();  # 转化成大写
            log.info("请求参数类型：%s" % parmsType)
            log.info("请求头：%s" % headers)
            log.info("请求参数：%s" % data)
            r = RunMethod()
            # res = r.run_method(method, url, data, headers)
            aa = str(len(headers) == 0)
            log.info("请求头是否为空：%s" % aa)
            datastr = len(data) != 0
            log.info("dataadsd：%s" % str(datastr))
            data = TestCase().newdata(data, myami)
            # 处理入参
            # if datastr:
            #     log.info("data不为空")
            #     data = TestCase().newdata(data,myami)
            #     # parmsType为json时；字典对象转换为json字符串
            #     if parmsType == 'json' or parmsType == 'JSON':
            #         data = ast.literal_eval(data)   # 转化成字典
            #         # data = json.loads(data)     # 字典对象转换为json字符串
            #     log.info("asdf2" + str(data))
            # else:
            #     log.info("data为空")
            res = r.run_method(method, parmsType, url, data, headers, myami)
            log.info("返回结果：%s" % res)
            flag = None
            for i in range(0, len(c)):
                checkPoint_dict = {}
                checkPoint_dict[c[i].split('=')[0]] = c[i].split('=')[1]
                # jsonpath方式获取检查点对应的返回数据
                list = jsonpath.jsonpath(res, c[i].split('=')[0])# 如果取不到将返回False # 返回列表
                log.info("jsonpath取值："+str(list))
                if str(list) != "False":
                    log.info("jsonpath取值成功" + str(list))
                    value = list[0]
                    check = checkPoint_dict[c[i].split('=')[0]]
                    log.info("检查点数据{}：{},返回数据：{}".format(i + 1, check, value))
                    print("检查点数据{}：{},返回数据：{}".format(i + 1, check, value))
                    # 判断检查点数据是否与返回的数据一致
                    flag = IsInstance().get_instance(str(value), str(check))
                    # flag = IsInstance().get_instance(value, check)
                    if not flag:
                        print("断言失败")
                        break;
                else:
                    log.info("jsonpath取值失败" + str(list))
                    flag = False
                    # log.info("flag值False为：" + flag)
                    break;
            ss = mywrite()
            log.info("最终flag值为：" + str(list))
            if flag:
                log.info("测试用例：{},测试通过++++++++++++++++++++++++++++++".format(caseRowNumber))
                # 响应入库
                log.info("用例成功执行响应入库")
                TestCase.putresponse(self, res, response)
                log.info("测试用例：{},测试通过++++++++++++++++++++++++++++++"
                         "++++++++++++++++++++++++++++++".format(caseRowNumber) + '\n')
                # 更改excel，需要关闭该excel
                ss.write(file_path, sheet_name, int(rowNumber) + 1, 15, "Pass")

                # ExcelData(file_path, sheet_name).write(rowNumber + 1, 15, "Pass")
            else:
                log.info("测试用例：{},测试失败------------------------------"
                         "------------------------------".format(caseRowNumber) + '\n')
                ss.write(file_path, sheet_name, int(rowNumber) + 1, 15, "Fail")
                # ExcelData(file_path, sheet_name).write(rowNumber + 1, 15, "Fail")
                self.assertTrue(flag,
                                msg="接口:" + url +
                                    "; 入参：" + str(data) +
                                    "; 响应：" + str(res) +
                                    "; 检查点数据与实际返回数据不一致。")
                # 断言
                # self.assertTrue(flag, msg="检查点数据与实际返回数据不一致")

        else:
            unittest.skip("不执行")

    def putresponse(self, res, response):
        # log.info("处理响应")
        if len(response) != 0:
            responseone = response.split(",")
            # log.info("responseone长度："+str(len(responseone)))
            for i in range(0, len(responseone)):
                # jsonpath方式获取检查点对应的返回数据
                if len(responseone[i]) != 0:
                    log.info("逗号分割后第:{} 个数据：{}".format(i + 1, responseone[i]))
                    list = jsonpath.jsonpath(res, responseone[i].split('=')[0])
                    myvalue = list[0]
                    mykey = responseone[i].split('=')[1]
                    myami[mykey] = myvalue
                    # log.info("key：{},value:{}".format(mykey, myvalue))
                else:
                    log.info("逗号分割后第:{} 个数据为空;不处理".format(i + 1))
            log.info("响应处理完毕")
        else:
            log.info("响应为空不处理")


    def newdata(self, data, myami):
        reg = "\\$\\{[a-zA-Z0-9]+\\}";  # 定义正则表达式
        regs = "[a-zA-Z0-9]+";  # 定义正则表达式
        log.info("data1:"+data)
        if '$' in data:
            log.info("data12:")
            # 正则提取
            nn = re.findall(reg, data)
            for i in nn:
                log.info("data:" + i)
                nnn=re.findall(regs, i)
                dataone=nnn[0]
                if dataone in myami:
                    data = data.replace(i,myami[dataone])
        log.info("更改后data:"+data)
        return data

if __name__ == '__main__':
    # unittest.main()
    # Alt+Shift+f10 执行生成报告

    # 报告样式1
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_path = r"D:\PycharmProjects\AutoTest\result\report.html"
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner(stream=f, title="Esearch接口测试报告", description="测试用例执行情况", verbosity=2)
        runner.run(suite)
    # data = "id=${roleid}"
    # newdata(data)
