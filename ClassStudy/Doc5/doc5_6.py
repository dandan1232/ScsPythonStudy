# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 14:16
# @Author  : Lindand
# @File    : doc5_6.py
# @Description :
# 判断闰年：用户输入年份year, 判断是否为闰年?
# 注：能被4整除但不能被100整除的 或者 能被400整除，那么就是闰年。

year = int(input("请输入年份："))  # 从键盘输入年份，转换为整数类型

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("%d年是闰年" % year)
else:
    print("%d年不是闰年" % year)
