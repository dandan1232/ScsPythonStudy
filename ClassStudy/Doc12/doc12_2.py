# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 13:50
# @Author  : Lindand
# @File    : doc12_2.py
# @Description :定义三个类Circle、Square和Rectangle，它们都有求面积的Area()方法。
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return math.pi * (self.radius ** 2)


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def Area(self):
        return self.side_length ** 2


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width


'''定义了三个类：Circle、Square和Rectangle。每个类都有一个构造方法__init__来初始化相应的属性。
在Circle类中，只有一个属性radius，表示圆的半径。Area()方法计算并返回圆的面积，使用了数学模块中的π值和幂运算。
在Square类中，有一个属性side_length，表示正方形的边长。Area()方法计算并返回正方形的面积，通过将边长平方来实现。
在Rectangle类中，有两个属性length和width，分别表示矩形的长和宽。Area()方法计算并返回矩形的面积，通过将长乘以宽来实现'''

# 创建一个圆对象，并计算面积
circle = Circle(5)
circle_area = circle.Area()
print("圆的面积：", circle_area)  # 输出：圆的面积： 78.53981633974483

# 创建一个正方形对象，并计算面积
square = Square(7)
square_area = square.Area()
print("正方形的面积：", square_area)  # 输出：正方形的面积： 49

# 创建一个矩形对象，并计算面积
rectangle = Rectangle(4, 6)
rectangle_area = rectangle.Area()
print("矩形的面积：", rectangle_area)  # 输出：矩形的面积： 24
