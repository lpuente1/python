#creating function
def end_withzeros(scores):
    total = 0
    
#creating parameter to add values in a list ending in 0 
    for num in scores:
        if num %10 == 0:
            total += num
    return total 

#list of scores
scores =  [200, 456, 300, 100, 234, 678]
#displaying sum of values in a list
list = end_withzeros(scores)
print(list)