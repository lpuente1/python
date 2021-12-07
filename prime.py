#define variables 
#user input for first and second prime numbers  
prime_1 = int(input("Enter the first prime number: "))
prime_2 = int(input("Enter the second prime number: "))

#print the prime numbers in ranges of prime1 and prime 2
print("The prime numbers between" , prime_1 and prime_2, "are: ")

#loop to calculate range of prime numbers
for number in range (prime_1, prime_2 + 1):
        if number > 1:   #if input number is greater than 1
            for i in range (2, number):   
                if (number % i) == 0: #if input number is equal to zero
                    break           #end loop

            else:                   
                print(number)  #print output


