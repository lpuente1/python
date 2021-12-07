#creating function
def writelines():

        #opening diary.txt in read mode
        outfile = open('diary.txt', 'r') 
        line = outfile.readlines()  
        count = 0
        
        #creating rule to only show sentences that have a letter P
        for words in line:
            if words [0] == "P" or words [0] == "p":
                print (line)  #print lines with a letter P
        outfile.close()  #close file


