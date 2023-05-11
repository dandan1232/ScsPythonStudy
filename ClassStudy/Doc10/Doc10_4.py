# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 13:50
# @Author  : Lindand
# @File    : Doc10_4.py
# @Description :
# 现在请你录入某班学生的语文、数学和英语成绩，并统计三门课程的平均成绩，打印结果。用下面的格式将数据存储到scores.txt文件：
# 张三 90 80 95
# 李四 70 80 88
# 王五 85 70 90
# 赵六 88 66 77
# ……
# 这里，每行是一个学生，第一列是学生姓名（假定姓名不重复），第二列语文成绩、第三列数学成绩、第四列英语成绩，列之间用空格隔开。
# 现在要求编写程序
# （1） 首先提示用户输入学生的姓名，然后依次提示输入语文、数学和英语的成绩，直到输入姓名为end时结束输入，保存数据到scores.txt文件；
# （2）  读取scores.txt文件，计算出语文、数学、英语三门课程的班级平均分，在屏幕上输出结果。

# 打开文件以追加模式写入数据
with open("date/scores.txt", "a") as f:
    while True:
        # 提示用户输入学生的姓名，如果输入为end，则结束输入
        name = input("请输入学生姓名（输入end结束录入）：")
        if name == "end":
            break
        # 提示用户输入语文、数学和英语成绩
        chinese = input("请输入语文成绩：")
        math = input("请输入数学成绩：")
        english = input("请输入英语成绩：")
        # 将学生姓名和成绩写入文件中
        f.write(name + " " + chinese + " " + math + " " + english + "\n")

# 读取scores.txt文件
with open("date/scores.txt", "r") as f:
    # 初始化语文、数学和英语总分和学生人数的计数器
    chinese_sum = 0
    math_sum = 0
    english_sum = 0
    count = 0
    # 逐行读取文件中的每一行，对于每一行，分别统计语文、数学和英语总分，并累加到总的计数器中
    for line in f:
        count += 1
        fields = line.split()
        chinese_sum += int(fields[1])
        math_sum += int(fields[2])
        english_sum += int(fields[3])
    # 计算语文、数学和英语的平均分
    chinese_avg = chinese_sum / count
    math_avg = math_sum / count
    english_avg = english_sum / count
    # 打印语文、数学和英语的平均分
    print("语文平均分：", chinese_avg)
    print("数学平均分：", math_avg)
    print("英语平均分：", english_avg)
