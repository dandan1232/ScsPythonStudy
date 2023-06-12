# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 21:23
# @Author  : Lindand
# @File    : doc2_2.py
# @Description :编写一个程序，提示用户输入三角形的三个顶点(x1，y1)、（x2，y2）、（x3，y3），
# # 然后计算三角形面积，这里假定输入的三个点能构成三角形。将面积输出到屏幕，要求输出占7列，保留2位小数，左对齐。

import math

x1, y1 = input("1(,):").split(",")
x2, y2 = input("2(,):").split(",")
x3, y3 = input("3(,):").split(",")
x1, y1 = float(x1), float(y1)
x2, y2 = float(x2), float(y2)
x3, y3 = float(x3), float(y3)

# a=abs(max(x1,x2,x3)-min(x1,x2,x3))*abs(max(y1,y2,y3)-min(y1,y2,y3))
# s1=(abs(x1-x2)*abs(y1-y2))/2
# s2=(abs(x3-x1)*abs(y3-y1))/2
# s3=(abs(x3-x2)*abs(y3-y2))/2
# print(a-s1-s2-s3)
# print(a,s1,s2,s3)


side1 = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
side2 = math.sqrt(math.pow(x3 - x1, 2) + math.pow(y3 - y1, 2))
side3 = math.sqrt(math.pow(x3 - x2, 2) + math.pow(y3 - y2, 2))
s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
# area1=format(area,".2f")
print(format(area,"<7.2f"))

print("{:<7}{:>7.2f}".format("面积：", area))
