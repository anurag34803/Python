a = input()                          # string given by user
a = a.split()
b = str()

for i in a:
    if(i not in b):
        b = b + i
        print(i,end=" ")
