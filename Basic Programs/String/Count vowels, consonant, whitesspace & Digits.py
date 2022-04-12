string = input("Enter String\n")
vowels = ['A','E','I','O','U','a','e','i','o','u']
 
consonant = whitespace = digits = vowel = 0                    # Creating Variables for store count


for i in string:
    
    if(i in vowels):
        vowel +=1
    
    elif(i == ' '):
        whitespace +=1
    
    elif(i >= '1' and i<='9'):
        digits +=1

    else: 
        consonant +=1
        
print("Vowel is : ",vowel)
print("Consonant is : ",consonant)
print("Digits is : ",digits)
print("whitespace is : ",whitespace)
