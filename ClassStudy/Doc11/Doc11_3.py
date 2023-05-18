# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 13:51
# @Author  : Lindand
# @File    : Doc11_3.py
# @Description :设计一个Rectangle类，属性为左上角和右下角的坐标，编写方法，实现根据坐标计算矩形的面积。
# 坐标数据提醒用户通过键盘录入，打印计算面积的结果。

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_area(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        area = width * height
        return area


# 获取用户输入的坐标数据
x1 = int(input("请输入左上角 x 坐标："))
y1 = int(input("请输入左上角 y 坐标："))
x2 = int(input("请输入右下角 x 坐标："))
y2 = int(input("请输入右下角 y 坐标："))

# 创建Rectangle对象
rectangle = Rectangle(x1, y1, x2, y2)

# 计算并打印矩形的面积
area = rectangle.calculate_area()
print("矩形的面积为:", area)
