a = (2,4,7,9)
b = (4,6,8,9)
c = list()                              # creation of list which store common elements of tuples

for i in a:
    if(i in b):
        c.append(i)
        

c = tuple(c)
print (c)
