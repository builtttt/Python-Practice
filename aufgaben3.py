# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:47:06 2022

@author: jirap
"""

def make_matrix(n):
    matrix = []
    for i in range(1,n+1):
        liste = []
        for j in range(1,n+1):
            liste.append(i+j)
        matrix.append(liste)
    return matrix

'----------------------------------------------------------------'

import math as m

def f1(x):
    return m.sin(x)

def f2(x):
    return 2*m.pi*x

def concatenate_functions(outer,inner):
    def concat(x):
        return(outer(inner(x)))
    return(concat)

#print(concatenate_functions(f1, f2)(0.25))
'-------------------------------------------------------------------'

def filter_liste(funktion,liste):
    for element in liste:
        if not funktion(element):
            liste.remove(element)
    return liste

liste1 = [0,1,2,3,4,5,6,7,8,9]
liste2 = ['Hallo','alle','zusammen']

print(filter_liste(lambda x : x % 2 == 0, liste1))

print(filter_liste(lambda x : len(x) <= 5, liste2))

