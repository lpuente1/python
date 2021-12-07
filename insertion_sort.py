#creating array
def insert_sort(a):  #defining variable

    #creating insertion sort
    for i in range(1, len(a)): # Travel through all array elements
 
        #maintains order of sequence
        key = a[i]  
        sort = i-1       
        while sort >= 0 and key < a[sort] :  #if number is greater than key, 
                a[ + 1] = a[sort]          #move one position ahead
                sort -= 1              #number in insertion sort should be less or equal to 1
        a[sort + 1] = key            #output 
 

a = [3, 5, 9, 16, 20]  #array of numbers in sequential order
insert_sort(a)  #insert array

print ("Array of numbers from lowest to greatest: ")  #printing array order
for i in range(len(a)):  #returning numbers in a sequence
    print ("% d" % a[i])  #print array from lowest to highest 