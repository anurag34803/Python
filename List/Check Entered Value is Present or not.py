'''
we also use index() method in list for searching item.
index() function returns index of first element with specified value but it generate error if value is not present.
'''
a = [1,2,3,4,5,6,7,8,9]
b = int(input("Enter Values\n"))


if( (b in a) == True):
    print("Entered Value is Present")
    
else:
    print("Entered Value is not Present")
