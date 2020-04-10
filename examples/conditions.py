# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:08:37 2020

@author: Novin
"""


     
for n in range(2, 22):
 
 for x in range(2, n):
   if n % x == 0:
       print(n, 'equals', x, '*', n//x)
       break
   
       
 
 # loop fell through without finding a factor
      
       
   
 # loop fell through without finding a factor
   


       
       
       
'''
for n in range(1, 10):
   if n % 2 == 0:
       print (n,'is even')
   else:
       print(n,'is odd')
       
       
 for x in range(2, 10):
        if n % x == 0:
            print(n, 'equals', x , '*', n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
a , b = 90 , 80
print('a is greater!') if a > b else print('equal!') if a==b else print('a is less than!') 



words = ['apple' , 'banana' , 'cherry','orange','straberry']

print('exist') if 'onion' in words else print('not exist')



if 'onion' not in words:
    print('not exist!')
    
 
if 'cherry' in words:
    print('exist!')
    
    
 


x , y = 102 , 98

if x < y: 
    print('x is less than y!')
    
else:
    print('x is greater or equal to y!')
    
    
    
    



x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    
    
    '''