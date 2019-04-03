#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math


def location(n):
    if n < 1:
        return '请输入正整数！'
    if n == 1:
        return 0
    c = (int)(math.ceil(math.sqrt(n)) / 2)  # 该数值在第几个方框上，从0算起
    # print('c=',c)
    # c_d_count=2*c+1#the count in single direction in c rectangle
    # print('c_d_count=',c_d_count)
    # c_count=8*c#c>0
    # print('c_count=',c_count)
    # c0=(2*c-1)*(2*c-1)+2*c#(c,c)
    # c1=(2*c-1)*(2*c-1)+4*c#(-c,c)
    # c2=(2*c-1)*(2*c-1)+6*c#(-c,-c)
    # c3=(2*c+1)*(2*c+1)#(-c,-c)
    # print(' c0=',c0,' c1=',c1,' c2=',c2,' c3=',c3)
    d = math.floor((n - (2 * c - 1) * (2 * c - 1) - 1) / (2 * c))
    # print('d=',d)
    if d == 0:
        x = c
        y = c - ((2 * c - 1) * (2 * c - 1) + 2 * c - n)
    elif d == 1:
        x = c - (n - (2 * c - 1) * (2 * c - 1) - 2 * c)
        y = c
    elif d == 2:
        x = -c
        y = c - (n - (2 * c - 1) * (2 * c - 1) - 4 * c)
    elif d == 3:
        x = c - ((2 * c + 1) * (2 * c + 1) - n)
        y = -c
    # print('location:(',x,',',y,')')
    return math.floor(abs(x)) + math.floor(abs(y))


while (1):
    n = input('input:')
    rlt = location(int(n))
    print('Answer:', rlt)
