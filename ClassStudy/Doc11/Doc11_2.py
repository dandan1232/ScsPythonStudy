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

'''定义了一个名为Dog的类。该类具有三个实例属性：name、color和weight。我们使用__init__方法来初始化这些属性。bark方法用于打印狗叫声。
然后，我们创建一个名为my_dog的Dog实例，传入名字、毛色和体重作为参数。最后，我们通过调用my_dog.bark()来触发狗的叫声输出。
请注意，类方法可以通过类的实例来调用，如my_dog.bark()。这里my_dog是一个Dog类的实例，通过该实例调用bark方法。'''