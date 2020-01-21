n = int(input("Enter numbers : "))
arr = []
sum =0 
for i in range(0,n):
    arr.append(int(input(f"Enter number {i+1} : " )))

for i in arr:
    sum+=i
print(f'Sum of All numbers are : {sum}')