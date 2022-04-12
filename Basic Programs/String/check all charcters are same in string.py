string = input("Enter String\n")
string = string.upper()                 # python is caee sensitive so we convert string in uppercase 
character = string[0]                   # store any character for match with all character
condition = 1

for i in string:
    
    if(character is i):
        continue
    
    else:
        condition = 0
        break
    
if(condition):
    print("All characters are same")
    
else:
    print("All characters are not same")
