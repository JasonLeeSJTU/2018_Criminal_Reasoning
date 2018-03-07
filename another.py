#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: another.py

@time: 2018/3/7 15:22

@desc:

'''

# copy from zhihu.com @ 杨航锋
'''
作者：杨航锋
链接：https://www.zhihu.com/question/68411978/answer/335904367
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

import itertools

A = 'A'
B = 'B'
C = 'C'
D = 'D'

def Q1():
    options = {
        A : A,
        B : B,
        C : C,
        D : D
    }
    option = options[answer[1]]
    return option == answer[1]
def Q2():
    options = {
        A : C,
        B : D,
        C : A,
        D : B
    }
    option = options[answer[2]]
    return option == answer[5]
def Q3():
    options = {
        A : answer[3],
        B : answer[6],
        C : answer[2],
        D : answer[4]
    }
    option = options[answer[3]]
    values = list(options.values())
    values.remove(option)
    return option not in values
def Q4():
    options = {
        A : (answer[1], answer[5]),
        B : (answer[2], answer[7]),
        C : (answer[1], answer[9]),
        D : (answer[6], answer[10])
    }
    option = options[answer[4]]
    return option[0] == option[1]
def Q5():
    options = {
        A : answer[8],
        B : answer[4],
        C : answer[9],
        D : answer[7]
    }
    option = options[answer[5]]
    return option == answer[5]
def Q6():
    options = {
        A : (answer[2], answer[4]),
        B : (answer[1], answer[6]),
        C : (answer[3], answer[10]),
        D : (answer[5], answer[9])
    }
    option = options[answer[6]]
    return len(set(list(option) + [answer[8]])) == 1
def Q7():
    options = {
        A : answer.count(C),
        B : answer.count(B),
        C : answer.count(A),
        D : answer.count(D)
    }
    option = options[answer[7]]
    return option == min(options.values())
def Q8():
    options = {
        A : answer[7],
        B : answer[5],
        C : answer[2],
        D : answer[10]
    }
    option = options[answer[8]]
    return abs(ord(option) - ord(answer[1])) != 1
def Q9():
    options = {
        A : answer[6],
        B : answer[10],
        C : answer[2],
        D : answer[9]
    }
    option = options[answer[9]]
    assume1 = (answer[1] == answer[6])
    assume2 = (option == answer[5])
    return assume1 != assume2
def Q10():
    options = {
        A : 3,
        B : 2,
        C : 4,
        D : 1
    }
    option = options[answer[10]]
    keys = options.keys()
    counts = [answer.count(key) for key in keys]
    return option == abs(max(counts) - min(counts))

answers = itertools.product([A, B, C, D], repeat=10)
for answer in answers:
    answer = ['']+list(answer)
    if Q1() and Q2() and Q3() and Q4() and Q5() and \
       Q6() and Q7() and Q8() and Q9() and Q10():
            print('  '.join(answer))
            break