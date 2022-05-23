# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:28:18 2022

@author: jirap
"""
def schrittZahl(n):
    schritte = 0
    while n != 0:
        if n % 3 == 0:
            n += 4
            schritte += 1
        elif n % 3 != 0:
            if n % 4 == 0:
                n /= 2
                schritte += 1
            elif n % 4 != 0:
                n -= 1
                schritte += 1
    return schritte

def neueSumme(x):
    result = 0
    for i in range(0,x):
        if i % 7 == 0 and i % 3 != 0:
            result += i
    return result

def osterdatum(x):
    k = x // 100
    m = 15 + (3*k+3)//4 -(8*k+13)//25
    s = 2-(3*k+3)//4
    a = x%19
    d = (19*a+m)%30
    r = (d+a//11)//29
    og = 21+d-r
    sz = 7-(x+x//4+s)%7
    oe = 7-(og-sz)%7
    os = og + oe
    
    return os

def winnerList(A,B):
    punkteA = 0
    punkteB = 0
    for i in range(len(A)):
        if A[i]>B[i]:
            punkteA += 1
        elif A[i] < B[i]:
            punkteB += 1
            
    if punkteA > punkteB:
        return 'A'
    elif punkteA < punkteB:
        return 'B'
    else:
        return '0'
    


