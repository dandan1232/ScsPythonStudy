# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 13:41
# @Author  : Lindand
# @File    : doc9_4.py
# @Description :
# 当前路径下有一个文本文件students_data.txt，该文件中保存了若干个学生的信息，每个学生信息占一行，
# 学生信息从左到右分别为：学号(int类型)、姓名(字符串类型)、年级(int类型)，各信息以空格分隔。编写程序完成如下功能：
# a)	打开文件，读取所有学生信息。
# b)	输出所有学生信息到屏幕上，要求每个学生信息占一行，学号占10列、左对齐，姓名占15列、左对齐，年级占5列、右对齐。
# c)	对所有学生根据其学号按照从小到大排序。
# d)	删除指定学号的学生，该学号由用户键盘输入。

def main():  # 主函数，用来访问学生信息
    global c  # 存放排序后的信息
    b = []  # 将文件中信息添加进去
    with open("date/students_data.txt", "r", -1, 'utf-8') as f1:
        print("%-10s%-15s%5s" % ("学号", "姓名", "年级"))
        for line in f1:  # 按每行读取
            line.replace("\n", "")  # 去掉换行符
            a = line.strip()  # 去掉两端空格
            a = line.split()  # 将每行中的信息以空格分割
            b.append((int(a[0]), a[1], (a[2])))  # 将分割的信息添加进去
    c = sorted(b, key=lambda x: x[0])  # 按学号进行排序
    for i in c:
        print("%-10d%-15s%5s" % (i[0], i[1], i[2]))  # 遍历格式化输出


def dels(n):  # 删除学生信息函数
    for i in c:
        if i[0] == int(n):  # 判断要删除的学号是否存在
            c.remove(i)
            print("----删除成功！----")
            print("删除后为：")
            print("%-10s%-15s%5s" % ("学号", "姓名", "年级"))
            for i in c:
                print("%-10d%-15s%5s" % (i[0], i[1], i[2]))
            break
    else:
        print("学号错误!删除失败")


main()
num = (input("输入要删除的学号："))
dels(num)
