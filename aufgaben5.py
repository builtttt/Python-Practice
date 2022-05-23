# -*- coding: utf-8 -*-
"""
Created on Mon May  9 12:30:58 2022

@author: jirap
"""
hello = [('h',1),('e',1),('l',2),('o',1)]

vorkomm = 3
letter = 'b'

newword = (letter,vorkomm)
print(newword)
(hello.append(newword))
print(hello)

def charFrequenz(x):
    
    result = []
    
    satzzeichen = '!@#$%^&*()_., '
    for zeichen in satzzeichen:
        x = x.replace(zeichen,'')
    
    x = sorted(x)
    
        
    for i in range(len(x)):
        letter = x[i]
        vorkomm = 1
        for j in range(len(x)):
            if i != j:
                if x[i] == x[j]:
                    vorkomm += 1
                    
        result.append((letter,vorkomm))
             
    result = list(dict.fromkeys(result))
    
    return result
            
    
    
    
    


def summe(m,n):
    if m == n:
        return m
    elif m > n: #Error
        return 0
    else:
        return m + summe(m+1,n)



def ggT(m,n): 

   if m == n:
       return(m)
   
   elif m > n:
      return ggT(m-n,n) 
   
   elif n > m:
      return ggT(m,n-m)
  

def vielfaches(n,liste):
    modifiedlist = []
    for e in (liste):
        if e % n != 0 or e == n:
            modifiedlist.append(e)
    return modifiedlist


def sieb(n):
    mylist = []
    for i in range(2,n+1):
        mylist.append(i)
        
    
    teiler = 2
    while teiler != n+1:
        
        mylist = vielfaches(teiler, mylist)   
        teiler += 1
        
    return mylist
        










