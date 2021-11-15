# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     operate_excel
   Description :    读写Excel
   Author :       xiaoyu
   date：          2021/11/9
-------------------------------------------------
"""
import json
import openpyxl
import os

excel_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "testdata", "case.xlsx")


class OperateExcel:
    def __init__(self, sheet_name):
        """
        初始化数据
        """
        self.path = excel_path
        self.wb = openpyxl.load_workbook(self.path)
        self.wk = self.wb[sheet_name]

    def read_excel(self):
        """
        将所有用例按字典格式转化后加入到列表data_all
        :return: data_all
        """
        # 通过遍历行读取Excel数据并将每行加入到一个列表row_list，wk.rows相当于一个生成器
        data_list = []
        for row in self.wk.rows:
            row_list = []
            for cell in row:
                row_list.append(cell.value)
            data_list.append(row_list)
        # 将第一行与非第一行进行字典转化,并加入到列表data_all
        data_all = []
        for i in data_list[1:]:
            x = dict(zip(data_list[0], i))
            data_all.append(x)
        return data_all

    def write_excel(self, actually, result, **header):
        """
        将actually和result分别写入H和I列，并按最大行进行遍历写入
        :param result:要传入的测试结果，如:pass，failed，blocked
        :param actually:要写入的数据
        :param header:非必传，传值为字典型,如：token="token"
        :return:
        """
        for i in range(2, self.wk.max_row + 1):
            # 如果不传header则往H和I列写入实际返回结果和测试结果
            if header == {}:
                self.wk["H{}".format(i)] = actually
                self.wk["I{}".format(i)] = result
                self.wb.save(self.path)
                self.wb.close()
            else:
                # 将header转化为json字符串
                self.wk["E{}".format(i)] = json.dumps(header)
                self.wk["H{}".format(i)] = actually
                self.wk["I{}".format(i)] = result
                self.wb.save(self.path)
                self.wb.close()
