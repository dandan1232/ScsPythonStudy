# -*- coding: utf-8 -*-
# @Time    : 2023/6/11 20:45
# @Author  : Lindand
# @File    : month.py
# @Description :输出月份

months="JanFebMarAprMayJunJulAugSepOctNovDec"
n=input("请输入月份(1-12)：")
pos=(int(n)-1)*3
monthResult=months[pos:pos+3]
print("月份简写是%s"%monthResult)
