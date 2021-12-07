def factorial(n):  #defining factorial number
       
    if n == 0:    #if number is equivalent to 0
        return 1   #output is 1
      
    return n * factorial(n-1)   #output is number chosen x factorial 
   
num = 5;               #factorial is 5
print("Factorial of", num, "is",   #output of factorial 
factorial(num))        #output is 120