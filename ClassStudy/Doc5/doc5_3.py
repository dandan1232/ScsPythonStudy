# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 14:05
# @Author  : Lindand
# @File    : doc5_3.py
# @Description :从键盘输入任意3个整数，使用分支语句嵌套，按从大到小的顺序输出。

# 如果a大于等于b，则进入第一个分支；
# 如果b大于等于c，则说明a最大，c最小，输出a、b、c；
# 如果a大于等于c，则说明a最大，b次之，c最小，输出a、c、b

a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))

if a >= b:
    if b >= c:
        print(a, b, c)
    elif a >= c:
        print(a, c, b)
    else:
        print(c, a, b)
else:
    if a >= c:
        print(b, a, c)
    elif b >= c:
        print(b, c, a)
    else:
        print(c, b, a)
