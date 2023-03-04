# 4) Simple calculator in python using if else

print("Enter the first Number")
a = int(input())

print("Enter the second Number")
b = int(input())

print("Enter whoch opearation you wants to perform : '+','-','*','/','**' ")
c = input()

if a==45 and b==3 and c=='*':
    print(555)
elif a==56 and b==9 and c=='+':
    print(77)
elif a==56 and b==4 and c=='/':
    print(4)
elif c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='**':
    print(a**b)
else:
    print("Something went wrong")
    
    