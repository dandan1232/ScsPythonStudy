# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 19:54
# @Author  : Lindand
# @File    : doc4_4.py
# @Description :
# 创建一个有关雇员姓名和编号处理的程序。从键盘输入一组雇员姓名和编号。在此基础上实现：
# a)	按照雇员姓名的顺序输出数据，雇员姓名显示在前面，后面是对应的雇员编号。
# b)	按照雇员编号的顺序输出数据，雇员编号显示在前面，后面是对应的雇员姓名。

'''不会'''

employee_info = {}
employee_data = input("输入，姓名编号，按照 ：")
while employee_data != "":
    name, number = employee_data.split()
    employee_info[name] = number
    print(employee_info[name])
    employee_data = input("按照空格结束:")

print("name顺序")
for name in sorted(employee_info.keys()):
    print(name, employee_info[name])

number_name_dict = {v: k for k, v in employee_info.items()}
print(number_name_dict)

print("number顺序排序")
for number in sorted(number_name_dict.keys()):
    print(number, number_name_dict[number])
