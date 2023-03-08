# To chake the given number is prime or not

print("Prime number or not")
print("")
a =int(input("Enter the number : "))
r = 0
for i in range(2,a):
    if(a%i==0):
        r=1
        break
    else:
        r=0
        break
if(r==0):
    print("it is a prime number")
else:
    print("It is not a prime number")


