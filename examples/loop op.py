# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 06:20:01 2020

@author: Novin
"""

a = 0

while a < 10:
   print(a)
   a = a + 1








'''
words = ['apple' , 'banana' ,'orange' , 'cherry' ,'straberry']

quality = ['A','B','A+','C','B+' , 'C+']

   
for count,ele in enumerate(words,100): 
    print (count,ele)
    
    


for item in words[2:5]:
    print(item)
    

zObj = set( zip(words,quality))
print(zObj)
print('================')
for a,q in zip(words,quality):
    print(a,q)
    print('Fruite is %s with %s quality'%(a,q))
    print( '{0} with {1} quality.'.format(a,q))




for item in enumerate(words):
    print(item)

     

for item in enumerate(words,20):
    print(item)

print('=========================')     
    
for i in range(2,5):
    words[i] = 'peach'

print(words)

for i in reversed (range(len(words))):
    print(i,words[i])


sortedList = sorted(words)
print(sortedList)


studentId = ['A32001','A32002','A32003','A32004']

for item in studentId:
    print(item)
    
    
print('=========================')  

for i in range(len(studentId)):
    studentId[i] = studentId[i] +'_class'
    
print(studentId)




for item in words:
    print(item)
    item = 'peach'

print(words)

print('=========================')

for i in range(len(words)):
    print(words[i])
    words[i] ='peach'

print(words)




for item in words[-3:]:
    print(item)
    
    
print('------------------')
    

for item in words[:-3]:
    print(item)

for item in enumerate(words):
    print(item)
    
    
    
    
    
for count,ele in enumerate(words,100): 
    print (count,ele)
    
    
for item,qu in zip(words,quality): 
     print ("Fruite :  %s     Quality : %s" %(item,qu)) 
     
     
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
    
    
    
for i in reversed(range(1, 10, 2)):
   print(i)
    
    
   
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
    '''