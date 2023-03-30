# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 14:20
# @Author  : Lindand
# @File    : doc4_4.py
# @Description :
# 创建一个有关雇员姓名和编号处理的程序。从键盘输入一组雇员姓名和编号。在此基础上实现：
# a)	按照雇员姓名的顺序输出数据，雇员姓名显示在前面，后面是对应的雇员编号。
# b)	按照雇员编号的顺序输出数据，雇员编号显示在前面，后面是对应的雇员姓名。

# 初始化一个空字典，用于存储雇员信息
employee_info = {}

# 从键盘输入一组雇员姓名和编号，以空格分隔
employee_data = input("请输入雇员姓名和编号，以空格分隔：")

# 将输入的雇员姓名和编号分割开并添加到字典中
while employee_data != "":
    name, number = employee_data.split()
    employee_info[name] = number
    employee_data = input("请输入雇员姓名和编号，以空格分隔，如果输入完成请直接回车：")

# 按照雇员姓名的顺序输出数据
print("按照雇员姓名的顺序输出数据：")
for name in sorted(employee_info.keys()):
    print(name, employee_info[name])

# 创建一个新字典，键和值互换，用于按照雇员编号的顺序输出数据
number_name_dict = {v: k for k, v in employee_info.items()}

# 按照雇员编号的顺序输出数据
print("按照雇员编号的顺序输出数据：")
for number in sorted(number_name_dict.keys()):
    print(number, number_name_dict[number])
