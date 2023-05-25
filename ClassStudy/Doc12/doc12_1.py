# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 13:46
# @Author  : Lindand
# @File    : doc12_1.py
# @Description :
# 定义一个圆类，具有圆心位置、半径、颜色等属性，编写构造方法和其他成员函数，能够设置属性值，获取属性值，计算周长和面积。

import math


class Circle:
    def __init__(self, center_x, center_y, radius, color):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color

    def set_center(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y

    def set_radius(self, radius):
        self.radius = radius

    def set_color(self, color):
        self.color = color

    def get_center(self):
        return self.center_x, self.center_y

    def get_radius(self):
        return self.radius

    def get_color(self):
        return self.color

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


'''在上面的代码中，定义了一个Circle类。构造方法__init__用于初始化圆的属性值：圆心位置（center_x和center_y）、半径（radius）和颜色（color）。
接下来，定义了一系列成员函数来设置和获取属性值。例如，set_center函数用于设置圆心位置，get_center函数用于获取圆心位置。
同样地，定义了set_radius、get_radius、set_color和get_color函数。
最后，定义了两个函数calculate_circumference和calculate_area来计算圆的周长和面积，分别使用了数学模块中的π值和幂运算。'''
# 现在，创建一个圆的对象，并使用定义的成员函数来设置属性值、获取属性值，以及计算周长和面积。
# 创建一个圆对象
my_circle = Circle(0, 0, 5, 'red')

# 获取圆心位置
center = my_circle.get_center()
print("圆心位置：", center)  # 输出：圆心位置： (0, 0)

# 设置半径
my_circle.set_radius(7)

# 获取半径
radius = my_circle.get_radius()
print("半径：", radius)  # 输出：半径： 7

# 计算周长
circumference = my_circle.calculate_circumference()
print("周长：", circumference)  # 输出：周长： 43.982297150257104

# 计算面积
area = my_circle.calculate_area()
print("面积：", area)  # 输出：面积： 153.93804002589985
