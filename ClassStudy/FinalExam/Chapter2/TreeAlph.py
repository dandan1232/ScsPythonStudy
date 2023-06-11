# -*- coding: utf-8 -*-
# @Time    : 2023/6/11 20:32
# @Author  : Lindand
# @File    : TreeAlph.py
# @Description : 三个单词，按字典顺序输出

s=input("x,y,z=")
x,y,z=s.split(",")
if(x>y):
    x,y=y,x
if(x>z):
    x,z=z,x
if(z>y):
    z,y=y,z
print(x,y,z)