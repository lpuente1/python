import sys
#array of numbers and defining variable
select_sort = [100, 2, -36, 175, -28,  4,  112, 34, 164, -187]    
 

#creating selection sort 
for i in range(len(select_sort)):   #for every number displayed in the selection sort
    minimum = i      #display lowest number
    for m in range(i+1, len(select_sort)):  #for every number displayed in the selection sort
        if select_sort[minimum] > select_sort[m]:   #if first number is greater than second number
            minimum = m     #display lowest number

#change minimum element with first element
    select_sort[i], select_sort[minimum] = select_sort[minimum], select_sort[i]   
 
#printing array order
print ("Array of numbers from lowest to greatest: ")  
for i in range(len(select_sort)):   #returning numbers in a sequence
    print("%d" %select_sort[i]),  #print array from lowest to highest