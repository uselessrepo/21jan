n = int(input("Enter numbers : "))
arr = []

for i in range(0,n):
    arr.append(int(input(f"Enter number {i+1} : " )))

num = int(input("Enter a number to search : "))
if num in arr:
    print("number is in array")
else:
    print("number is not in array")