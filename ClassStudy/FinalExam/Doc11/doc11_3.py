# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 20:31
# @Author  : Lindand
# @File    : doc11_3.py
# @Description :
# 设计一个Rectangle类，属性为左上角和右下角的坐标，编写方法，实现根据坐标计算矩形的面积。
# 坐标数据提醒用户通过键盘录入，打印计算面积的结果。


class Renctangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def area(self):
        h = abs(self.y1 - self.y2)
        w = abs(self.x1 - self.x2)
        area = h * w
        return area


a = int(input("1:"))
b = int(input("2:"))
c = int(input("3:"))
d = int(input("4:"))
result = Renctangle(a, b, c, d)
area1 = result.area()
print(area1)
