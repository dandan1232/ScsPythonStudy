# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 21:54
# @Author  : Lindand
# @File    : Built_InFunction.py
# @Description :68个内置函数

# 数学运算
print(bin(10))
print(hex(10))
print(oct(10))
print("______________")
print(abs(-2))
print(divmod(4, 3))  # 返回商和余数 4//3 4%3
print(round(8.3))
print(round(8.5))
print(round(9.5))
print(pow(3, 2, 4))  # 3的2次方对4取余 9%4
print(min(3, 5, 7, 1, 0, -2))
print(max(3, 5, 7, 1, 0, -2))

# 序列
# (1)列表和元组
print(list((1, 2, 3, 4, 5, 6, 7, 8)))
print(tuple([1, 2, 3, 4, 5, 6, 7, 8]))

# (2)相关内置函数
lst = "以雷霆击碎黑暗"
it = reversed(lst)
print(list(lst))
print(list(it))

print(lst[1:3:1])

s = slice(1, 5, 1)
print(lst[s])

# (3)字符串
print(str("像风一样") + "--薛之谦")

s = "念安"
print(format(s, "<20"))
print(format(s, ">20"))
print(format(s, "^20"))

print(format(3, 'b'))  # 二进制
print(format(11, 'o'))  # 八进制
print(format(11, 'd'))  # 十进制
print(format(11, 'x'))  # 十六进制小写
print(format(11, 'X'))  # 十六进组织大写
print(format(97, 'c'))  # unicode转换
print(format(11, 'n'))
print(format(11))  # 十进制

print(format(1234564492831723432, 'e'))
print(format(123456789, '0.2e'))
print(format(123456789, '0.2E'))
print(format(1.23456749, 'f'))
print(format(1.23456789, '0.2f'))
print(format(1.23456789, '0.10f'))
print(format(1.23456789e+18, 'F'))
