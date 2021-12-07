#creating dictionaries
courses = {} 
semesters_offered = {}
def Merge(dictionary1, dictionary2):
    return(dictionary2.update(dictionary1))

choice = 1   #user has to select one choice
while choice !=0:
    #print users choice
    print('\nMenu')
    print('1. Add a record')
    print('2. Search a record')
    print('3. Change a record')
    print('4. Delete a record')
    print('0. Quit')
    choice = int(input('Enter your choice: '))  #select number

    #if user chooses option 1 
    if choice == 1: 
        Course_Name = input('Enter Course Name:')  #enter course name 
        Course_ID = int(input('Enter your 4 digit course ID:'))  #enter course ID
        if Course_Name:              #if course name exists, tell user it exists
            print('Course Name Already Exists')     
        else:   #if course does not exist
            courses[Course_Name] = Course_ID  #add record
            print('Record Added')   #record added
    

    #if user chooses option 2
    if choice == 2:   
        Course_ID = int(input('Enter your 4 digit course ID:'))  #enter course ID
        if Course_ID == 2333:   #if course name is 2333
            print('Scripting Languages')  #print class is called Scripting Languages
    

    #if user chooses option 3
    if choice == 3:
       Course_Name = input('Enter Course Name:')  #enter course name 
       Course_ID = int(input('Enter your 4 digit course ID:'))  #enter course ID 
    else:
        print('Record Changed')    #record changed
   

    #If user chooses option 4
    if choice == 4:
        Course_Name = input('Enter Course Name:')  #enter course name 
        Course_ID = int(input('Enter your 4 digit course ID:'))  #enter course ID
    else:
            print('Course Name: 2333- Scripting Languages, Fall 2021')   #course name and ID will show 
            print('Record Deleted')   #record deleted
    

    #if user chooses option 0
    if choice == 0:
        print ('Goodbye')   #exit program 
        quit()    #quit program 
