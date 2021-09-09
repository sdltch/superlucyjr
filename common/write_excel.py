import os
import time

from openpyxl import load_workbook
from self import self


class mywrite:
    def write(self, myexcel, myshell, rowNum, colNum, results):
        # wb = load_workbook("D:/testdata/gitami/pythonami/pythontest/data/接口自动化测试.xlsx")
        # wb2 = wb['测试用例']
        # wb2.cell(2, 13, '333')
        # wb.save("D:/testdata/gitami/pythonami/pythontest/data/接口自动化测试.xlsx")  # 保存
        wb = load_workbook(myexcel)
        wb2 = wb[myshell]
        wb2.cell(rowNum, colNum, results)
        wb.save(myexcel)  # 保存
        wb.close()  #关闭
        print("成功")

if __name__ == '__main__':
    file_path = "D:/testdata/gitami/pythonami/pythontest/data/接口自动化测试.xlsx"
    file_path = "D:/testdata/gitami/pythonami/superlucyjr/data/接口自动化测试.xlsx"
    sheet_name = '测试用例'
    ss = mywrite()
    ss.write(myexcel=file_path, myshell=sheet_name, rowNum=2, colNum=15, results='passone')

