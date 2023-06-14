# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 19:46
# @Author  : Lindand
# @File    : Fabonaci.py
# @Description :

def fabonaci(n):
    if n<=0:
        return []
    elif n==1:
        return [1]
    elif n==2:
        return [1,2]
    else:
        squence=fabonaci(n-1)
        next_num=squence[-1]+squence[-2]
        squence.append(next_num)
        return squence

num=int(input("n:"))
result=fabonaci(num)
print(result)