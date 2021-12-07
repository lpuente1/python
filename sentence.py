text = input('Enter a string: ')       #string. user enters sentence

for letter in text:             #for every letter found in the text
    if not letter.isdigit():   # string converted to boolean. function takes off numbers in a sentence
        print(letter, end='')    #prints output without numbers

