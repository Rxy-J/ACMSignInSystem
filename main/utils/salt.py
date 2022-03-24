#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DK 
@File ：salt.py.py
@Author ：OrangeJ
@Date ：2021/11/25 10:59 
'''

import random

KEY_LIST = "abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890"


def genSalt(length: int = 6) -> str:
    salt = ""
    for i in range(length):
        salt += random.choice(KEY_LIST)

    return salt


if __name__ == "__main__":
    print(genSalt())
