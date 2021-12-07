#pseudocode
#import numpy
#create a vector with values from 0-20
#print original output 
#create a vector and change signs for values ranging from 9-15
#print modified output

#import numpy
import numpy as np
matrix = np.arange(21)   #vector using 21 values 
print("Vector:")   
print(matrix)            #output of original values 
matrix[(matrix >= 9) & (matrix <= 15)] *= -1   #creating vector to change signs for the numbers 
print("After changing the sign of the numbers ranging from 9 to 15, the output is:")  
print(matrix)   #output of new values 