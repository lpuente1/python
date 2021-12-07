#pseudocode
#create a book class 
#create a method
#create functions for each of the methods mentioned in the book class
#user input on how many records they want entered
#create a function to search for a book
#output results 
#create a function to search for a book using only IBSN 
#output result 
#create a function to delete a record
#output result 
#create a function to update a record 
#output result 
#close file


#creating a class and methods
class Book:
    def __init__(self, set_ibsn, set_name, set_price, get_ibsn, get_name, get_price, _str_ ):
        self.set_ibsn = set_ibsn
        self.set_name = set_name
        self.set_price= set_price
        self.get_ibsn = get_ibsn
        self.get_name = get_name
        self.get_price = get_price

#creating functions for each method and setting value
    
def set_ibsn (self,value):
    self.ibsn = value
  
def set_name(self,value):
    self.name = value
  
def set_price(self,value):
    self.price = value
  
def get_ibsn (self,value):
    self.ibsn  = value

def get_name (self, value):
    self.name = value

def get_price (self, value):
    self.price = value 

#asking user how many records they want to enter 
int(input('How many records do you want to enter?:  ')) 
print ("!")

#creating a function to search for a book
def search_book(): 

#input information for book 1
    get_ibsn = (int(input('Enter IBSN number :'))  #enter IBSN number 
    get_name = (int(input('Enter book name :'))  #enter book name 
    get_price = (int(input('Enter book price :'))  #enter book price

#input information for book 2
    get_ibsn = (int(input('Enter IBSN number :')  #enter IBSN number 
    get_name = (int(input('Enter book name :'))  #enter book name 
    get_price = (int(input('Enter book price :'))  #enter book price

#input information for book 3
    get_ibsn = (int(input('Enter IBSN number :')  #enter IBSN number 
    get_name = (int(input('Enter book name :'))  #enter book name 
    get_price = (int(input('Enter book price :'))  #enter book price

#output of results 
print
('IBSN number: 8175255766'
'Book name: Pyython Programming' 
'Book price: 49.00' )

print 
('IBSN number: 8123456790'
'Book name: C++ programming'
'Book price: 129.00' )

print 
('IBSN number: 9876543210'
'Book name: Learn Python'
'Book price: 350.00 ')

#searching for a book using IBSN 
get _ibsn: int(input('Enter IBSN to search: '))  #user nput
    print ('IBSN number: 8123456790'
    'Book name: C++ programming'
    'Book price: 129.00' )

#creating a function to delete a record
def delete_book():
    int(input('Enter IBSN to delete a record: ')) #user input
    print('Record deleted') #deletes record 

#creating a function to update record information 
def update_book():
    int(input('Enter IBSN to update price: '))  #user input
    int(input('Enter new price of book: '))
    print('Record updated')  #updates record 

#close file
class Book () 
    


