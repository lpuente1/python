#defining variable and creating menu display
def show_choices():      
#menu of options
                    print('\nMenu')
                    print('1. add')
                    print('2. substract')
                    print('3. multiply')
                    print('4. divide')
                    print('5. exit')

def add(a,b):   #add equation
    return a + b

def substract(a,b):  #substract equation
    return a - b 

def multiply(a, b):  #multiply equation
    return a * b 

def divide( a, b):  #divide equation
    return a / b

def main():
    while(True):
        show_choices()      #menu of options will display to the user
        choice = input('Enter choice(1-5):')   #user will choose between options 1-5


def choice():

#if user chooses option 1
    if choice == 1:
        x = int(input('Enter first number: '))    
        y = int(input('Enter second number: '))
        print('Sum =', add(x,y))   #output will be sum of both numbers

#if user chooses option 2
    elif choice == 2:
     x = int(input('Enter first number: '))
     y = int(input('Enter second number: '))
     print('Difference =', substract(x,y))  #output will be difference of both numbers

#if user chooses option 3
    elif choice == 3:
     x = int(input('Enter first number: '))
     y = int(input('Enter second number: '))
     print('Product =', multiply(x,y))   #output will be multiplication of both numbers

#if user chooses option 4
    elif choice == 4:
     x = int(input('Enter first number: '))
     y = int(input('Enter second number: '))
     if y == 0:
        print('Error! Divide by zero!')   #user has to divide any first number by zero
     if x == 0:
        print('Quotient =', divide(x,y))  #output will be quotient of both numbers

#if user chooses option 5
    elif choice == '5':
         break     #program will quit

#if user chooses a number that is not 1-5
    else:
        print('Invalid input')   

 main() #this will take user back to the beginning of the program
