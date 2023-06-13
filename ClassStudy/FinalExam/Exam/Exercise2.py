# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 19:33
# @Author  : Lindand
# @File    : Exercise2.py
# @Description :
# 公园前 5 世纪，我国数学家张丘建在《算经》中提出百钱百鸡问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一，百钱买百鸡，问鸡翁、母、雏各几何？
# 意思是：一只公鸡值五钱，一只母鸡值三钱，三只鸡子值一钱，用一百钱恰好买一百只鸡，问公鸡、母鸡和鸡子各几只？请用循环求解。

def solve_q():
    for x in range(0, 21):
        for y in range(0, 34):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                return x, y, z
    return None


result = solve_q()
if result:
    x, y, z = result
    print("{0},{1},{2}".format(x, y, z))
else:
    print("无解")
