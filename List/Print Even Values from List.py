a = input("Enter Values\n")      
a = a.split(",")

b = list()     # create empty list which store even values

for i in a :
    i = int(i)
    if(i%2==0):
        b.append(i)
        
print(b)
