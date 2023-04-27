# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 13:51
# @Author  : Lindand
# @File    : doc8_5.py
# @Description :
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指0、1、1、2、3、5、8、13、21、34、.......，用数学表达式为F(0)=0，F(1)=1，F(n)=F(n - 1)+F(n - 2)，n ≥ 2。
# 编写一个递归函数，求解Fibonacci数列的第n项。编写测试程序，从键盘输入n，输出Fibonacci数列第n项的值。并输出斐波那契数列的前10项。

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("请输入n："))

# 输出斐波那契数列的前10项
fibonacci_list = [fibonacci(i) for i in range(10)]
print("斐波那契数列前10项：", fibonacci_list)

# 输出斐波那契数列第n项的值
print("斐波那契数列第{}项的值为：{}".format(n, fibonacci(n)))
