while True:
    import sys
    a_1 = 0
    b_1 = 0
    c_1 = 0
    a_2 = 0
    c_2 = 0
    d = 0
    temp_1 = 0
    a = input('第一个数,退出请输入exit')
    b = input()
    c = input()
    c = int(c)
    a = int(a)
    if a_1 == 0 and c_1 == 0:
        if b == '*':
            print(a*c)
        elif b == '-':
            print(a-c)
        elif b == '+':
            print(a+c)
        elif b == '/':
            print(a/c)
