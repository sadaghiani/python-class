-----------------------------
#1. Write a Python program to count the number of characters (character frequency) in a string
#	Sample String : google.com'
#	Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 
	
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
#3. Write a Python program to count the occurrences of each word in a given sentence
#4. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form
 
