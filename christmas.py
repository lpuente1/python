#enter the number of rows for christmas tree
row = int(input("Enter number of rows: "))
#print number of rows 
print(str(row))

#loop to print rows and asterisks
#shape of tree and asterisks will be determined by number chosen by the user
for i in range(row):
    for s in range(row, i, -1):
        print(end=" ")      
    for j in range(i+1):   
        print(end="* ")     

    print() #output 

