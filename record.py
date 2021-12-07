import pickle

#Creating functions for student ID, student name, and grades

def set_data():
    std_id = int(input(' Enter student ID: '))
    std_name = int(input(' Enter student name: '))
    grades = int(input('Enter grade: '))
    print()

#Creating dictionary
    student = {}
    student['std_id'] = std_id 
    student['std_name'] = std_name 
    student['grades'] = grades

    return student

#creating function to allow the display of student id, student name and grades
def display_data(student): 
    print('Student ID:', student ['std_id'])
    print('Student name:', student['std_name'])
    print('Grades', student['grades'])
    print ()

#creating function to write records
#opening file in binary mode for writing
def write_record():
    outfile = open('student.dat', 'ab')

    pickle.dump(set_data(), outfile)

    outfile.close() #closing file

#creating function to read records
#opening file in binary mode for reading
def read_records():
    infile = open('student.dat)','rb')
    
    #read to the end of the file
    while True:
        try:
            student = pickle.load(infile)
            display_data(student)  
        except EOFError:
            break
        infile.close  #closing file

#Creating function to search records 
#opening file in binary mode for searching
def search_record():
    infile = open('student.dat', 'rb')
    std_id = int(input("Enter student ID to search: "))
    flag = False

    #read to the end of the file
    while True:
            try:
                student = pickle.load(infile)

                #display a record if found
                if student['stu_id'] == std_id:
                  display_data(student)
                  flag = True
                  break 
            except EOFError:
                    break 
    #if record is not displayed and found
    if flag == False:
        print('Record not found')
        print()
        infile.close()  #closing file

#displaying menu of options
    def show_choices():
        print('Menu')
        print('1. Add Record')
        print('2. Display Record')
        print('3. Search a Record')
        print('4. Exit')

    #show choices to user
    def main():
        while(True):
            show_choices()
            choice = input('Enter choice(1-4):')
            print()

            #if user chooses option 1
            if choice == '1':
                write_record()

            #if user chooses option 2
            elif choice == '2':
                read_records()
            
            #if user chooses option 3
            elif choice == '3':
                search_record()

            #if user chooses option 4
            elif choice == '4':
                break 

            #if user chooses a number that is not between 1-4
            else:
                print ('Invalid input')

    main()  #take user back to main function