# -*- coding: utf-8 -*-
# @Time    : 2023/6/11 20:08
# @Author  : Lindand
# @File    : TreePrint.py
# @Description :三位数输入并输出各个位上的数字

num=input("请输入一个三位数数字：")
num=int(num)
a,b = divmod(num,100)
print(a)
print(b)
b,c=divmod(b,10)
print(a,b,c)


a=x=y=10