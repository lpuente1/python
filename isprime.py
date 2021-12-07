#defining variable 
def isPrime(number):
    for i in range (2, number): #display every second number after 101
        if number % i == 0:  
            return False   #if a number is not prime, the argument will display as false
        return True  #if a number is prime, the argument will display as true

#defining variable
def main():
        for n in range(100,500):  #range 
            if isPrime(n):
                print(n, end= '')   #output numbers

main()   #this will take the user back to the beginning of the program 

