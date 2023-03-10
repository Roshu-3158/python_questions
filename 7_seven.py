# To chake the given number is prime or not
# Python also allows us to use the else condition with for loops without if condition

print("Prime number or not")
print("")
k="y"
while(k != "n"):
    a = int(input("Enter your number : "))
    for i in range(2,a):
        if(a==1):
            print("not prime not composite")
        elif(a%i==0):
            print("Not a Prime number")
            break
    else:
        print("Prime number")    
    k=input("do you wants to continue ? y/n :")