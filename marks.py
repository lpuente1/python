marks = int(input('Enter your marks in Computer Science: '))  #integer converted to string. user enters marks 

if marks>=90:        #if mark is greater than or equal to 90
    grade = 'A'      #grade is an A
elif marks>=80:      #if mark is greater than or equal to 80
    grade = 'B'      #grade is a B
elif marks>=70:      #if mark is greater than or equal to 70
    grade = 'C'      #grade is a C
elif marks>=60:      #if mark is greater than or equal to 60
    grade = 'D'      #grade is a D
else:                #if mark is lower than 60
    grade = 'F'      #grade is an F

print('Your grade is',grade)    #prints letter grade of mark