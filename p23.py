# 23.	Write a program to check if the given number is within a user specified range
x=int(input("Enter upper bound : "))
y=int(input("Enter lower bound : "))
n = int(input("Enter value : "))
if n>=x and n<=x:
    print('number is within range')
else:
    print("number is not in range")