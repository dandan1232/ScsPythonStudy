# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 13:57
# @Author  : Lindand
# @File    : doc7_7.py
# @Description :
# 恺撒密码，加密方法是将明文字母向左（或向右）移动一个固定数目的位置，所得即为密文字母。
# 如当偏移量是左移3时，明文字母表：ABCDEFGHIJKLMNOPQRSTUVWXYZ，加密后的密文字母表：DEFGHIJKLMNOPQRSTUVWXYZABC，解密密钥就是右移3位。
# 例如，明文是：THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
# 则密文：WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
# 要求编写一个加密函数encryption， 传入一个明文字符串，以及向左的偏移量值，返回加密过的密文；
# 再编写一个解密函数decryption , 传入一个密文，以及解密的密钥（即上一步加密时的那个偏移量值），返回解密后的明文。
# 在测试函数中给出函数调用，要求用户从键盘上输入明文和密钥，假设用户输入的都是大写（如果不是，请自行转换为大写）。

def encryption(plain_text, shift):
    # 将明文转换为大写
    plain_text = plain_text.upper()

    # 初始化密文
    cipher_text = ""

    # 加密每个字符
    for char in plain_text:
        if char.isalpha():
            # 计算偏移后的字符
            offset_char = chr((ord(char) - 65 + shift) % 26 + 65)
            cipher_text += offset_char
        else:
            # 非字母字符直接添加到密文中
            cipher_text += char

    return cipher_text


def decryption(cipher_text, shift):
    # 将密文转换为大写
    cipher_text = cipher_text.upper()

    # 初始化明文
    plain_text = ""

    # 解密每个字符
    for char in cipher_text:
        if char.isalpha():
            # 计算偏移前的字符
            offset_char = chr((ord(char) - 65 - shift) % 26 + 65)
            plain_text += offset_char
        else:
            # 非字母字符直接添加到明文中
            plain_text += char

    return plain_text


# 从键盘上获取明文和密钥
plain_text = input("请输入明文：")
shift = int(input("请输入偏移量："))

# 加密明文
cipher_text = encryption(plain_text, shift)
print(f"密文：{cipher_text}")

# 解密密文
plain_text = decryption(cipher_text, shift)
print(f"解密后的明文：{plain_text}")
