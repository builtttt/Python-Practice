# -*- coding: utf-8 -*-
"""
Created on Fri May  6 22:03:48 2022

@author: jirap
"""


def swap(N):
    n = str(N)
    front = n[0]
    last = n[-1]
    middle = ''
    for i in range(2,len(n)):
        
        middle += n[-i]

    swap = last + middle + front
    
    return swap



def isPalindrom(n):
    nlower = str(n).lower()
    
    if nlower == swap(nlower):
        return 1
        
    else:
        return 0
    
    
def findString(a,b,n):
    lenght = len(b)
    vorkomm = 0
    for i in range(len(a)):
        if a[i:i+lenght] == b:
            vorkomm += 1
            position = i
            
            if vorkomm == n:
                return position
    else:
        return -1       
    
'''
51-5 Ungefähr 1 Uhr
6-21 Ungefähr viertel nach 1 Uhr
31-45
45-60
'''
    
def vageUhrzeit(n):
    minute = int(n[3:5])
    hour = int(n[0:2])
    if minute < 8:
        return 'Ungefähr {} Uhr!'.format(hour)
    elif minute >= 53:
        return 'Ungefähr {} Uhr!'.format(hour+1)
    elif minute >= 8 and minute < 23:
        return 'Ungefähr viertel nach {}!'.format(hour)
    elif minute >= 23 and minute < 38:
        return 'Ungefähr halb {}!'.format(hour+1)
    elif minute >= 38 and minute < 53:
        return 'Ungefähr viertel vor {}!'.format(hour+1) 
    
    


def insertElem(myinsert,position,mylist):
    return mylist.insert(position,myinsert)

def delElem(position,mylist):
    del mylist[position]
    return mylist

def popElem(position,mylist):
    mylist.pop(position)
    return mylist

def sortList(sort,mylist):
    if sort == 1:
        return mylist.sort()
    elif sort == 2:
        return mylist.sort(reverse=True)

def appendElem(myappend,mylist):
    return mylist.append(myappend)    

    
    

   
            
        