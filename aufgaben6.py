# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:49:19 2022

@author: jirap
"""

def bibliotest(x):
        result = []
        for i in range(len(x)):
            
            bestellenwert = x[i][2]*x[i][3]
            round(bestellenwert,4)
            
            if bestellenwert < 100:
                y = (x[i][0],round(bestellenwert,4) + 10)
                result.append(y)
            
        
            else:
                y = (x[i][0],bestellenwert)
                result.append(y)
                
        return result

print(bibliotest([["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80],
              ["77226", "Head First Python, Paul Barry", 3, 32.95]]))


def howmuch(x):
    bestellenwert = round(x[2]*x[3],4)
    if bestellenwert < 100:
        return bestellenwert + 10
    else:
        return bestellenwert

def biblio(liste):
    
    bestellenwert = list(map(lambda x : howmuch(x) ,liste))
    nummer = list(map(lambda x : x[0],liste))
    
    result = list(zip(nummer,bestellenwert))
    
    return result


   

print(biblio([["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80],
              ["77226", "Head First Python, Paul Barry", 3, 32.95]]))



def kapitalWerttest(wert,zinsatz,jahr):
    
    dec = zinsatz/100
    return wert*(1+dec)**jahr

def kapitalWert(wert,zinsatz,jahr):
    
    for i in range(jahr):
        
        wert = wert + wert*(zinsatz/100)
        
    return wert 

def k(k,z,j):
	d = k+z/100*k
	e = d+z/100*d
	if j ==1:
		return(d)
	elif j >1:
		return(e)
    
    
print(kapitalWert(1000,5,3))
print(k(1000,5,3))
    



def querSumTest(n):
    nummer = str(n)
    result = 0
    for i in nummer:
        result += int(i)
    return result
 



    
def querSum(n):
    x = str(n)
    if len(x) == 0:
        return 0
    else:
        i = len(x)
        neuex = x[0:i-1]
        return int(x[i-1]) + querSum(neuex)
    

print(querSumTest(123))
print(querSum(123))
    


0,1,1,2,3,5,8,13,21


def findfibo(n):
    liste = [0,1]
    for i in range(n-1):
        nachstefibo = liste[i]+liste[i+1]
        liste.append(nachstefibo)
    
    return liste[len(liste)-1]



def fib_indexTest(n):
    
    i = 0
    while n >= findfibo(i):
        
        if n == findfibo(i):
            return i
        else:
            i += 1
    return -1
        
    
def fib_index(n):
    return 0

print(fib_indexTest(13))
print(fib_indexTest(79))


    
        
        
        
    
       

