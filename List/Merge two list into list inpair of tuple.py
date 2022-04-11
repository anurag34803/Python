a = [2,4,7,9]
b = [4,6,8,9]

# output -: [ (2,4), (4,6), (7,8), (9,9)]

length = len(a)
c = list()                             # creation of list which store tuples

for i in range(0,length):
    d = list()
    d.append(a[i])
    d.append(b[i])
    d = tuple(d)
    c.append(d)  

print (c)
