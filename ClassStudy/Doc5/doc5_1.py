# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 13:30
# @Author  : Lindand
# @File    : doc5_1.py
# @Description :
# 小明带着N元钱去买酱油。
# 酱油15块钱一瓶，商家进行促销，每买3瓶送1瓶，或者每买5瓶送2瓶。
# 请问小明最多可以得到多少瓶酱油。N的数值由用户输入，并且一定是整数。


# 获取用户输入的钱数
n = int(input("请输入钱数："))

# 根据商家的促销活动计算酱油瓶数
bottles = n // 15  # 首先计算小明可以直接购买的酱油瓶数

# 然后分别考虑每种促销活动对酱油瓶数的增加量
if bottles >= 3:  # 每买3瓶送1瓶
    bottles += bottles // 3
if bottles >= 5:  # 每买5瓶送2瓶
    bottles += (bottles // 5) * 2

# 输出结果
print("小明最多可以得到%d瓶酱油。" % bottles)
