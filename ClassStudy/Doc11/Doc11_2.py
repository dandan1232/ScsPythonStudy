# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 13:45
# @Author  : Lindand
# @File    : Doc11_2.py
# @Description :定义一个Dog类，实例属性有名字（name）、毛色（color）、体重（weight），方法为叫（bark），通过类名调用该方法时输出“wang！Wang！”
class Dog:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def bark(self):
        print("wang! Wang!")


# 创建一个Dog实例
my_dog = Dog("十七", "白色", 7)

# 调用bark方法
my_dog.bark()
