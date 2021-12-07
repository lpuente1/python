#importing string module
import string

#creating string
string = "scripting languages"

#creating a parameter to find out the total amount of characters in the sentence scripting languages
#If character is already in dictionary, increment count
#if character is not in dictionary, add as key and a value of 1 
char = {}
for i in string:  
    if i in char:  
        char[i] += 1 
    else:         
        char[i] = 1 

#output 
print("Count of characters for 'scripting languages' is: " + str(char))
