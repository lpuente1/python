#pseudocode
#create a txt file
#create a variable to open the file
#open the txt file
#read from the txt file
#count is 0
#create logic to iterate through an array
#if the words in the array have the letter T 
#do not output the word
#if the words in the array do not have the letter T 
#output the word
#close file



def count_lines():  #create variable
    document = open("story.txt","r")  #read content from txt file
    count=0  #count is 0 
    for line in document:  #creating array 
        if line[0] not in 'T' or 't':  #if a line does not have a T
            count+= 1   #add and display word 
    document.close()  #close txt file
    print("The number of lines starting with 'T' are =",count)  #output of words not having the letter T

count_lines()  #close file