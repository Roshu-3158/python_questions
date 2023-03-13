#  Write a program to reverse an integer in Python. 

print("Write a program to reverse an integer in Python")
print(" ")
a = int(input("Enter the number : "))
print(f"Before reverse the number is : {a}")
reverse = 0
while a!=0 :
    reverse = reverse*10 + a%10
    a = (a//10)
print(f"After reverse the string is : {reverse}")


