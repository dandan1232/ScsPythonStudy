# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 13:55
# @Author  : Lindand
# @File    : Doc11_5.py
# @Description :设计一个Date类，属性包括year、month、day三个属性和能够实现取日期值、取年份、取月份、设置日期、输出日期的方法。
# 实例化一个对象d，参数是2022，5，19，设置日期是20，最后输出日期。

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_date(self):
        return self.year, self.month, self.day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def set_date(self, day):
        self.day = day

    def display_date(self):
        print(f"日期: {self.year}-{self.month}-{self.day}")


# 实例化一个Date对象
d = Date(2022, 5, 19)

# 输出当前日期
d.display_date()

# 设置日期为20
d.set_date(20)

# 输出修改后的日期
d.display_date()
