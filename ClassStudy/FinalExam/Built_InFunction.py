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
print(format(1.23456789e-2, 'F'))

# bytes()把字符转化成bytes类型
bs = bytes("像风一样", encoding="utf-8")
print(bs)

# bytearray()返回一个新字节数组
ret = bytearray("像风一样", encoding="utf-8")
print(ret)
print(ret[0])
ret[0] = 65  # 65是A
print(ret)

print(ord('a'))
print(chr(65))
print(ascii(98))  # 98
for i in range(20):
    print(chr(i), end=" ")

a = "薛之谦"
str = "像\n风一%s样，你靠近云\t就下%s降" % (a, 98)
print(str)
print(repr(str))

# 2.数据集合
dict = (2, 3, 6, "好的")
print(dict)
set = {"888", 23, "薛之谦"}
print(type(set))

list = [2, 43, 67, 85, 12, 75]
print(type(list))
print(sorted(list))
a = sorted(list, reverse=True)
print(a)

list = ["cc", "CC", "A", "m", "H"]


def f(s):
    return len(s)


l1 = sorted(list, key=f, reverse=True)
print(l1)

list = ["念安", "石二狗", "阿正", "aaa", 111, 0]
for index, el in enumerate(list, 1):
    print(index, end=" ")
    print(el, end=" ")

print("____________________")
print(all(list))

list1 = ["念安", "石二狗", "阿正", "aaa", 111, 0]
list2 = ["cc", "CC", "A", "m", "H"]
list3 = [2, 43, 67, 85, 12, 75]
for i in zip(list1, list2, list3):
    print(i,end="------")

#map返回True和False
#filter返回值
def func(i):
    return i % 2 == 1


lst = [2, 43, 67, 85, 12, 75]
l1 = map(func, lst)
print(type(l1))
print(l1)
print(list(l1))


def func():
    a = 10
    print(locals())
    print(globals())
    print("今天不太开心")


func()

for i in range(15, -1, -5):
    print(i)

lst = [1, 2, 6, 4, 2, 7, 8]
it = iter(lst)
print(it.__next__())
print(next(it))
print(next(it))
print(next(it))


s1=input("a+b:")
print(eval(s1))
s2="for i in range(5):print(i)"
print(exec(s2))

#  动态执行代码
exec("""
def func():
    print("aaa")
func()
""")


code1 = "for i in range(5): print(i)"
com1 = compile(code1, "", mode="exec")
exec(com1)

code2 = "3+4+5+6"
com2 = compile(code2, "", mode="eval")
print(eval(com2))

code3 = "name=input(':')"
com3 = compile(code3, "", mode="single")
exec(com3)
print(name)


print("aa", "cc", "ee", sep="+", end="@")

s = "今天不开心"
print(hash(s))
tup = (2, 4, 5, 7, 1)
print(hash(tup))
print(id(s))

f = open("D:\Study\ScsPythonStudy\ClassStudy\Doc10\date\TelephoneBook.txt", mode="r", encoding="utf-8")
f.read()

print(dir(tuple))
