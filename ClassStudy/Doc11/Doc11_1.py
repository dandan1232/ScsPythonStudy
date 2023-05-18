# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 13:44
# @Author  : Lindand
# @File    : Doc11_1.py
# @Description :
# 已知f(40)/(f(30)+f(20))  ，当f (n)＝1×2＋2×3＋3×4＋……＋n×(n＋1)时，求y的值。分别用面向过程的方法和面向对象的方法来写程序，体会二者的区别。

# 面向过程的方法
def calculate_f(n):
    result = 0
    for i in range(1, n + 1):
        result += i * (i + 1)
    return result


f40 = calculate_f(40)
f30 = calculate_f(30)
f20 = calculate_f(20)

y = f40 / (f30 + f20)
print("y的值为:", y)


# 面向对象的方法
class FunctionCalculator:
    def __init__(self):
        self.result = 0

    def calculate_f(self, n):
        self.result = 0
        for i in range(1, n + 1):
            self.result += i * (i + 1)

    def get_result(self):
        return self.result


f_calculator = FunctionCalculator()
f_calculator.calculate_f(40)
f40 = f_calculator.get_result()

f_calculator.calculate_f(30)
f30 = f_calculator.get_result()

f_calculator.calculate_f(20)
f20 = f_calculator.get_result()

y = f40 / (f30 + f20)
print("y的值为:", y)

'''两种方法的区别在于面向过程的方法中使用函数来实现计算逻辑，而面向对象的方法中使用类和方法。
面向对象的方法将相关的数据和方法封装在一个对象中，通过对象的方法进行计算和获取结果，使代码结构更加清晰和可维护。
另外，面向对象的方法更加符合面向对象的设计原则，如封装、继承和多态等，适用于复杂的程序和大型项目。
而面向过程的方法更加直观，适用于简单的程序和小规模的任务。'''
