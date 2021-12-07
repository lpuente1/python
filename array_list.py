#pseudocode
#import numpy
#add an array with random values
#function needs to convert to an array first 
#unction needs to convert to a list after 
#print output. final list needs to be equal 

#import numpy
import numpy as np
arr = [[0, 1], [6, 7]]    #creating array 
n = np.array(arr)  #convert to array 
a2 = n.tolist()  #convert to list
print(arr == a2)  #final list is equal