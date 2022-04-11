a = input("Enter String\n")
a = a.upper()
lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
condition = 1 

for i in lst:
    if(i in a):
        continue
    
    else:
        condition = 0
        break
 
if(condition):
    print("Given String Is Pangram")
    
else:
    print("Given String is not a Pangram")
