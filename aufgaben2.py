# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:20:39 2022

@author: jirap
"""

##Aufgaben 1

def check(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 0
    
def printIT(n):
    out = ''
    for i in range(1,n+1):
        out += str(i)
    return out

def ist_Schaltjahr(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def print_Quadrad(n):
    result = 0
    for i in range(n):
        result += n**2
    return result