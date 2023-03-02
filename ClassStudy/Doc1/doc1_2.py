# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 9:31
# @Author  : Lindand
# @File    : doc1_2.py
# @Description :
# 从键盘输入四个整数，并输出其中最大的数。


# if __name__ == '__main__':
#     num1 = input("第一个数字")
#     num2 = input("第二个数字")
#     num3 = input("第三个数字")
#     num4 = input("第四个数字")
#     a = [num1, num2, num3, num4]
#     print(max(a))

print("请输入需要比较的三个值，用空格隔开:")
def getMax(*a):

    m=a[0]
    for x in a:
        if x>m:
            m=x
    return m
s,d,f=map(int,input().split())
print("最大值:",max(s,d,f))

