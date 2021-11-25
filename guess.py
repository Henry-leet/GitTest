#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：guess.py
# @Version ：
# @Author  ：Henry Han
# @Date    ：2021/11/23 17:34 

import random


if __name__ == '__main__':
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break
    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')
