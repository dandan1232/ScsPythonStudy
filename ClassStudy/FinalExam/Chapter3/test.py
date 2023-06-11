# -*- coding: utf-8 -*-
# @Time    : 2023/6/11 20:35
# @Author  : Lindand
# @File    : test.py
# @Description :第3章 Python数据类型
import math

z = 1.23e-4 + 5.78e+89j
print(z.real)
print(z.imag)

print(int(4.7))

print("\"hh\\naaa")

print("%8d" % (123))


name="念安"
age=8
print("我叫{2}，今年{1}岁".format(name,age,"29"))

print('{0:2>8}'.format("abc"))


n=str("%.2f"%(math.pi))
print(n.rjust(7))



print(b'1ab')
