a = [1,2,3,3,3,4,4,5,6]                       
b = list()                         #Crate Empty List for store unique element

for i in a :
    if( (i not in b) == True):
        b.append(i)
    
print(b)

# Another Method without using of Another List

'''
a = [1,2,3,3,3,4,4,5,6]                       

for i in a:
    b = a.count(i)
    if(b>1):
        for j in range(1,b):
            a.remove(i)
print(a)
'''
