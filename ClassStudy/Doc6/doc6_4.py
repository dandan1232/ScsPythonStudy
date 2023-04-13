# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 13:48
# @Author  : Lindand
# @File    : doc6_4.py
# @Description :
# 循环提示用户输入一个整型数字n（n代表后续需要输入整型数的数量），将n个整型数加起来并输出，如果输入的是非整型数则提示当前的输入非法需要重新输入数值，如果输入‘n=0’代表退出程序，否则继续提示用户输入新的n。
# 例：
# Please input the number of numbers：（假设输入n=3）
# Please input number 1： (假设输入3)
# Please input number 2： (假设输入4)
# Please input number 3： (假设输入5)
# 输出：sum = 12
# Please input the number of numbers：
# …
# Please input the number of numbers：（假设输入n=0，则退出程序）


while True:
    try:
        n = int(input("Please input the number of numbers (input 'n=0' to exit): "))
        if n == 0:
            break
        total = 0
        for i in range(1, n+1):
            num = int(input("Please input number {}: ".format(i)))
            total += num
        print("sum =", total)
    except ValueError:
        print("Invalid input. Please input an integer.")