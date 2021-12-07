#pseudocode 
#import numpy
#create a matrix with dimensions 10 x 10
#create a vector in which elements on the border will be equal to 1
#add to previous vector and state inside border will be 0
#print output 

#import numpy
import numpy as np
matrix = np.ones((10, 10)) #state matrix dimensions
matrix[1:-1, 1:-1] = 0  #elements on border will be equal to 1, and elements inside will be equal to 0
print(matrix)  #output 