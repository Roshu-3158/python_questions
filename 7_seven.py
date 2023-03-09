# To chake the given number is prime or not

print("Prime number or not")
print("")
k="y"
while(k is not "n"):
    a = int(input("Enter your number : "))
    for i in range(a):
        if(a==1):
            print("not prime not composite")
        elif(a%2==0):
            print("Not a Prime number")
            break
        else:
            print("Prime number")
            break
    k=input("do you wants to continue ? y/n :")