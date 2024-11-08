# -*- coding: utf-8 -*-
import sys
while True:
    a_1 = 0
    b_1 = 0
    c_1 = 0
    a_2 = 0
    c_2 = 0
    a = 0
    b = 0
    c = 0
    d = 0
    temp_1 = 0
    a = input('第一个数')
    if a == 'exit' or a == 'EXIT':
        sys.exit()
    b = input('符号')
    c = input('第二个数')
    if a[0] == '0':
        a_2 = 1
    if c[0] == '0':
        c_2 = 1
    for i in range(len(a)):
        if a[d] != '1' and a[d] != '2' and a[d] != '3' and a[d] != '4' and a[d] != '5' and a[d] != '6' and a[d] != '7' and a[d] != '8' and a[d] != '9' and a[d] != '0':
            a_1 = 1
        d += 1
    d = 0
    for i in range(len(c)):
        if c[d] != '1' and c[d] != '2' and c[d] != '3' and c[d] != '4' and c[d] != '5' and c[d] != '6' and c[d] != '7' and c[d] != '8' and c[d] != '9' and c[d] != '0':
            c_1 = 1
        d += 1
    if b != '+' and b != '-' and b != '*' and b != '/' and b != '**':
        b_1 = 1
    if a_1 == 1 or c_1 == 1 or b_1 == 1 or a_2 == 1 or c_2 == 1:
        if a_1 == 1:
            print('第一位数不是整数')
        if c_1 == 1:
            print('第二位数不是整数')
        if b_1 == 1:
            print('符号输入错误,可用的符号为:1.*(乘法) 2.**(幂) 3./(除法) 4.+(加法) 5.-(减法)')
        if a_2 == 1:
            print('第一个数的第一个位置不能是0')
        if c_2 == 1:
            print('第二个数的第一个位置不能是0')
        continue
    c = int(c)
    a = int(a)
    if a_1 == 0 and c_1 == 0:
        if b == '**':
            temp = a
            for i in range(c-1):
                temp = temp*a
            print(temp)
            continue
        if b == '*':
            print(a*c)
            continue
        elif b == '-':
            print(a-c)
            continue
        elif b == '+':
            print(a+c)
            continue
        elif b == '/':
            temp_1 = a/c
            for i in range(len(str(temp_1))):
                if str(temp_1)[i] == '.':
                    temp_1_debug = i
                    break
            if str(temp_1)[temp_1_debug+1] == '0' and len(str(temp_1)) == temp_1_debug+2:
                print(str(temp_1)[:-2])
                sys.exit()
            print(a/c)
            continue