# To check type of char present in a string
print('Bestfriend777'.isalnum())            
print('nutan'.isalpha())
print('877'.isdigit())
print('nutankate'.islower())
print('NUTANKATE'.isupper())
print(' '.isspace())
print("I Am Nutan".istitle())
 
 
str=input("Enter the char: ")
if str.isalnum():
    print("Alpha numeric char")
    if str.isalpha():
        print("Alpha char")
        if str.isupper():
            print("Upper case char")
        else:
            print("Lower case char")    
    else:
        print("Numaric char")
elif str.isspace():
    print('It is a space char')
else:
    print("Is is not a space char")