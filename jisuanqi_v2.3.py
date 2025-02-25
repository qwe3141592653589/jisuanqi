# -*- coding: utf-8 -*-
import sys
while True:
    a_1 = 0 #第一个数输入判断，0为正确，1为不正确
    b_1 = 0 #符号输入判断，0为正确，1为不正确
    c_1 = 0 #第二个数判断，0为正确，1为不正确
    a_2 = 0 #第一个数是否已0开头，0为否，1为是
    c_2 = 0 #第二个数是否已0开头，0为否，1为是
    a = 0 #第一个数输入
    b = 0 #符号输入
    c = 0 #第二个数输入
    help = '可以用的指令:exit(退出)，help(帮助)所有指令均需要输入在第一个数的询问内,第一个数输入要运算的第一个数(幂输入底数)，符号需要输入可用的符号(可用的符号为:1.*(乘法) 2.**(幂) 3./(除法) 4.+(加法) 5.-(减法))，第二个数输入要运算的第二个数(幂输入次数)，所有输入数字部分必须为整数并且不得已0开头' #帮助手册内容
    temp_1 = 0 #除法运算时初步计算出结果的临时数据
    temp_1_debug = 0 #除法运算时初步计算结果中.的位置
    a = input('第一个数')
    if a == 'exit' or a == 'EXIT':
        sys.exit()
    if a == 'help' or a == 'EHLP':
        print(help)
        continue
    b = input('符号')
    c = input('第二个数')
    if a[0] == '0':
        a_2 = 1
    if c[0] == '0':
        c_2 = 1
    try:
        a = int(a)
    except ValueError:
        a_1 = 1
    try:
        c = int(c)
    except ValueError:
        c_1 = 1
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