# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 14:13
# @Author  : Lindand
# @File    : doc5_5.py
# @Description :
# 假设银行对1年期的存款利息计算法方法如下：如果存款金额I小于10万元，则按照1.5%的年利率计算利息；
# 如果存款金额I大于等于10万元，但小于50万元，则按照2%的年利率计算利息；
# 如果存款金额I大于等于50万元，但小于100万元，则按照3%的年利率计算利息；
# 如果存款金额大于等于100万元，则按照3.5%的年利率计算利息。现在从键盘输入一个整数表示存款金额，
# 请计算一年后的本金和利息总共有多少，将计算结果输出到屏幕上。


amount = int(input("请输入存款金额："))  # 从键盘输入存款金额，转换为整数类型

if amount < 100000:  # 存款金额小于10万元
    rate = 0.015  # 年利率为1.5%
elif amount < 500000:  # 存款金额大于等于10万元，但小于50万元
    rate = 0.02  # 年利率为2%
elif amount < 1000000:  # 存款金额大于等于50万元，但小于100万元
    rate = 0.03  # 年利率为3%
else:  # 存款金额大于等于100万元
    rate = 0.035  # 年利率为3.5%

interest = amount * rate  # 计算利息
total = amount + interest  # 计算本息和

print("一年后本金和利息总共有%d元" % total)  # 输出结果
