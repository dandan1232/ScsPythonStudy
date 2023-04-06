# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 14:18
# @Author  : Lindand
# @File    : doc5_7.py
# @Description :
# 鸡兔同笼问题：“今有鸡兔同笼，上有三十五头，下有九十四脚，问鸡、兔各几何？”
# 请用户输入头数和脚数，计算出鸡有几只，兔有几只。如果不能算出整数，提示数据有误


heads = int(input("请输入头数："))  # 从键盘输入头数，转换为整数类型
legs = int(input("请输入脚数："))  # 从键盘输入脚数，转换为整数类型

if legs % 2 != 0 or heads <= 0 or legs <= 0:
    print("数据有误！")
else:
    rabbits = (legs - 2 * heads) / 2
    chickens = heads - rabbits
    if rabbits < 0 or chickens < 0 or rabbits % 1 != 0 or chickens % 1 != 0:
        print("数据有误！")
    else:
        print("鸡有%d只，兔有%d只" % (chickens, rabbits))
