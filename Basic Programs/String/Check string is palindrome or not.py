"""A string is called a palindrome string if the reverse of that string is the same as the original string.
For example, radar , level , etc."""


string = input()                          # string given by user
reverse = string[::-1]                   # store reverse of string

if(string == reverse):
    print("Given string is Palindrome")
    
else:
    print("Given string is not a Palindrome")
