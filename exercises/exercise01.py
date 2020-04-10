-----------------------------
#1. Write a Python program to count the number of characters (character frequency) in a string
	
word = "google.com'"

characterFrequency = {} 
  
for i in word: 
    if i in characterFrequency: 
        characterFrequency[i] += 1
    else: 
        characterFrequency[i] = 1

print ("Count of all characters in word is :\n " +  str(characterFrequency)) 

-----------------------------
#2. Write a Python program to remove the characters which have odd index values of a given string

def oddValuesString(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result += str[i]
  return result

print(oddValuesString('python'))

-----------------------------
#3. Write a Python program to count the occurrences of each word in a given sentence
import string 

text = "Mango- banana, apple! pear Mango!"  

dic = {}

text = text.translate(text.maketrans("", "", string.punctuation))
text = text.strip() 
text = text.lower() 
text = text.split(" ") 

for word in text: 
  if word in dic: 
    dic[word] = dic[word] + 1
  else: 
    dic[word] = 1

print(dic)

-----------------------------
#4. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form

s = input()
words = [word for word in s.split(",")]
print( ",".join(sorted(list(set(words)))))

-----------------------------
#5. isPrime

for val in range(11, 25): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val)
