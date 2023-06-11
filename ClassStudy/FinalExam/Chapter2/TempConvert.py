# -*- coding: utf-8 -*-
# @Time    : 2023/6/11 19:54
# @Author  : Lindand
# @File    : TempConvert.py
# @Description :第二章 Python编程基础


Tem=input("请输入当前温度(C或F结尾，比如37C)：")
if Tem[-1] in ['C','c']:
    f=1.8*float(Tem[0:-1])+32
    print("转换为F:%.2fF"%f)
elif Tem[-1] in ['F','f']:
    f=(float(Tem[0:-1])-32)/1.8
    print("转化为C结尾度数%.2fC"%f)
else:
    print("重新输入")
