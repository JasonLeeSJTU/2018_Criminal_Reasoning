#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: main.py

@time: 2018/3/6 20:48

@desc:

'''
from itertools import zip_longest

# question 2
def check1(answer):
    if answer[1] == 0 and answer[4] == 2:
        return True
    if answer[1] == 1 and answer[4] == 3:
        return True
    if answer[1] == 2 and answer[4] == 0:
        return True
    if answer[1] == 3 and answer[4] == 1:
        return True

def check2(answer):
    if answer[2] == 0:
        if answer[2] != answer[5] and answer[2] != answer[1] and answer[2] != answer[3]:
            return True
    if answer[2] == 1:
        if answer[5] != answer[2] and answer[5] != answer[1] and answer[5] != answer[3]:
            return True
    if answer[2] == 2:
        if answer[1] != answer[2] and answer[1] != answer[5] and answer[1] != answer[3]:
            return True
    if answer[2] == 3:
        if answer[3] != answer[2] and answer[3] != answer[5] and answer[3] != answer[1]:
            return True

def check3(answer):
    if answer[3] == 0:
        if answer[0] == answer[4] and answer[1] != answer[6] and answer[0] != answer[8] and answer[5] != answer[9]:
            return True
    if answer[3] == 1:
        if answer[0] != answer[4] and answer[1] == answer[6] and answer[0] != answer[8] and answer[5] != answer[9]:
            return True
    if answer[3] == 2:
        if answer[0] != answer[4] and answer[1] != answer[6] and answer[0] == answer[8] and answer[5] != answer[9]:
            return True
    if answer[3] == 3:
        if answer[0] != answer[4] and answer[1] != answer[6] and answer[0] != answer[8] and answer[5] == answer[9]:
            return True

def check4(answer):
    if answer[4] == 0:
        if answer[7] == answer[4] and answer[3] != answer[4] and answer[8] != answer[4] and answer[6] != answer[4]:
            return True
    if answer[4] == 1:
        if answer[7] != answer[4] and answer[3] == answer[4] and answer[8] != answer[4] and answer[6] != answer[4]:
            return True
    if answer[4] == 2:
        if answer[7] != answer[4] and answer[3] != answer[4] and answer[8] == answer[4] and answer[6] != answer[4]:
            return True
    if answer[4] == 3:
        if answer[7] != answer[4] and answer[3] != answer[4] and answer[8] != answer[4] and answer[6] == answer[4]:
            return True

def check5(answer):
    if answer[5] == 0:
        if answer[1] == answer[7] and answer[3] == answer[7] and answer[0] != answer[7] and answer[5] != answer[7] \
            and answer[2] != answer[7] and answer[9] != answer[7] and answer[4] != answer[7] and answer[8] != answer[7]:
            return True
    if answer[5] == 1:
        if answer[1] != answer[7] and answer[3] != answer[7] and answer[0] == answer[7] and answer[5] == answer[7] \
            and answer[2] != answer[7] and answer[9] != answer[7] and answer[4] != answer[7] and answer[8] != answer[7]:
            return True
    if answer[5] == 2:
        if answer[1] != answer[7] and answer[3] != answer[7] and answer[0] != answer[7] and answer[5] != answer[7] \
            and answer[2] == answer[7] and answer[9] == answer[7] and answer[4] != answer[7] and answer[8] != answer[7]:
            return True
    if answer[5] == 3:
        if answer[1] != answer[7] and answer[3] != answer[7] and answer[0] != answer[7] and answer[5] != answer[7] \
            and answer[2] != answer[7] and answer[9] != answer[7] and answer[4] == answer[7] and answer[8] == answer[7]:
            return True

def check6(answer):
    a = answer.count(0)
    b = answer.count(1)
    c = answer.count(2)
    d = answer.count(3)

    re = min(a,b,c,d)

    if answer[6] == 0 and re == c:
        return True
    if answer[6] == 1 and re == b:
        return True
    if answer[6] == 2 and re == a:
        return True
    if answer[6] == 3 and re == d:
        return True

def check7(answer):
    if answer[7] == 0:
        if answer[6] != answer[0] and [6] != answer[0] + 1 and answer[6] != answer[0] - 1:
            return True
    if answer[7] == 1:
        if answer[4] != answer[0] and [4] != answer[0] + 1 and answer[4] != answer[0] - 1:
            return True
    if answer[7] == 2:
        if answer[1] != answer[0] and [1] != answer[0] + 1 and answer[1] != answer[0] - 1:
            return True
    if answer[7] == 3:
        if answer[9] != answer[0] and [9] != answer[0] + 1 and answer[9] != answer[0] - 1:
            return True

def check8(answer):
    if answer[8] == 0:
        if (answer[0] == answer[5] and answer[5] != answer[4]) or (answer[0] != answer[5] and answer[5] == answer[4]):
            return True
    if answer[8] == 1:
        if (answer[0] == answer[5] and answer[9] != answer[4]) or (answer[0] != answer[5] and answer[9] == answer[4]):
            return True
    if answer[8] == 2:
        if (answer[0] == answer[5] and answer[1] != answer[4]) or (answer[0] != answer[5] and answer[1] == answer[4]):
            return True
    if answer[8] == 3:
        if (answer[0] == answer[5] and answer[8] != answer[4]) or (answer[0] != answer[5] and answer[8] == answer[4]):
            return True

def check9(answer):
    a = answer.count(0)
    b = answer.count(1)
    c = answer.count(2)
    d = answer.count(3)
    least = min(a, b, c, d)
    most = max(a, b, c, d)
    re = most - least
    if answer[9] == 0 and re == 3:
        return True
    if answer[9] == 1 and re == 2:
        return True
    if answer[9] == 2 and re == 4:
        return True
    if answer[9] == 3 and re == 1:
        return True

def Ten2Four(x):
    res = []
    while x > 3:
        res.append(str(x % 4))
        x = x // 4
    if x:
        res.append(str(x))

    return ''.join(reversed(res))

# answer = [1,1,1,1,1,1,1,1,1,1] # initial answer for the 10 questions
answer = 0
temp = [0,0,0,0,0,0,0,0,0,0]
if __name__ == '__main__':
    # print(Ten2Four(99))
    # r = [int(x) for x in str(999)]
    # print(r)
    while True:
        # print('%d\n' % answer)
        lst = [int(x) for x in str(Ten2Four(answer))]
        lst = [x + y for x, y in zip_longest(reversed(temp), reversed(lst), fillvalue=0)][::-1]
        if not check1(lst):
            answer += 1
            continue
        if not check2(lst):
            answer += 1
            continue
        if not check3(lst):
            answer += 1
            continue
        if not check4(lst):
            answer += 1
            continue
        if not check5(lst):
            answer += 1
            continue
        if not check6(lst):
            answer += 1
            continue
        if not check7(lst):
            answer += 1
            continue
        if not check8(lst):
            answer += 1
            continue
        if not check9(lst):
            answer += 1
            continue

        break

    lst = [int(x) for x in str(Ten2Four(answer))]
    print(lst)