#pseudocode
#import numpy
#create a matrix with dimensions 5 x 5
#create an element on main diagonal equal 1,2,3,4,5
#print output

#import numpy
import numpy as np
matrix = np.ones((5, 5))  #dimensions of matrix
matrix= np.diagonal([1, 2, 3, 4, 5])  #adding measurements to the main diagonal
print(matrix)  #output 