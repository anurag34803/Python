string = input()                          # string given by user
lst = list()

for i in string:
    if(i not in lst):
        lst.append(i)
        print(i,"=",string.count(i))
