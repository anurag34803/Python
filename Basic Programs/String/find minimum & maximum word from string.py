a = "anu is ek good boy"
a = a.split()

max = a[0]                   
min = a[0]

for i in a:
    
    if(len(max) < len(i)):
        max = i
        
    elif(len(min) > len(i)):
        min = i
        
print(max)
print(min)
