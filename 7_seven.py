# To chake the given number is prime or not

print("Prime number or not")
print("")
a = int(input("Enter your number : "))
r=0
for i in range(2,a):
    if(a%2==0):
        print(" Not a Prime number")
        break
    else:
        print("Prime number")
        break

# if(r==0):
#     print("Prime number")
# else:
#     print("not a prime number")




