import sys
select_sort = [3, 5, 9, 16, 20]  #array of numbers and defining variable 

#creating selection sort
for i in range(len(select_sort)):   #for every number displayed in the selection sort
    minimum = i      #display lowest number
    for m in range(i+1, len(select_sort)):  #for every number displayed in the selection sort
        if select_sort[minimum] > select_sort[m]:   #if first number is greater than second number
            minimum = m     #display lowest number

    select_sort[i], select_sort[minimum] = select_sort[minimum], select_sort[i]   #change minimum element with first element.
 

print ("Array of numbers from lowest to greatest: ")  #printing array order
for i in range(len(select_sort)):   #returning numbers in a sequence
    print("%d" %select_sort[i]),  #print array from lowest to highest