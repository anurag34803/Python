a = input()                          # string given by user
a = a.split()

for i in a:
    if(i[-1] == 'S' or i[-1] == 's'):
        print(i)
