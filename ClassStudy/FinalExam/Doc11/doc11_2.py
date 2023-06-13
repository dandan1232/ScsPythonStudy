# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 20:26
# @Author  : Lindand
# @File    : doc11_2.py
# @Description :定义一个Dog类，实例属性有名字（name）、毛色（color）、体重（weight），方法为叫（bark），通过类名调用该方法时输出“wang！Wang！”
class Dog:
    def __init__(self, name, color, weight):
        self.name = name;
        self.color = color;
        self.weight = weight;

    def bark(self):
        print("wang!wang!")


my_dog = Dog("11", "11", 29)
my_dog.bark()
