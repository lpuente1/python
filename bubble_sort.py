#creating array
def bubble_sort(array):  #defining variables
    n = len(array)  
  
    #creating bubble sort
    for i in range(n):  # check all array elements

        for bubble in range(0, n-i-1): 
            
            if array[bubble] > array[bubble+1] :  #if the second number is greater than the one displayed first
                array[bubble], array[bubble+1] = array[bubble+1], array[bubble]  #swap numbers. then do the same with the next number
  
array = [1, 3, 6, 9, 20]  #displaying array from smallest to largest numbers
  
bubble_sort(array)    #sort bubble from lowest to highest
  
print ("Array of numbers from lowest to greatest:")  #printing array order
for i in range(len(array)):   #returning numbers in a sequence
    print ("%d" %array[i]),   #print array from lowest to highest order