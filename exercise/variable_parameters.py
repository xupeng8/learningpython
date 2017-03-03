#!/usr/bin/env python
#! -*- coding:utf-8 -*-

def cal(*num):
    sum = 0
    for n in num:
        sum = sum + n
    return sum

if __name__ == '__main__':
    print(cal(1,2,3))
    L = [4,5,6]
    print(cal(*L))

