def isLeap(year):
    if year % 4 == 0:
        print('is leap')
    else:
        print('is not leap')

while True:
    x = input("press Y/N to enter input ")
    if(x == 'Y' or x == 'y'):
        year = int(input("Enter Year : "))
        isLeap(year)
    else:
        break

print('program exited with exit code 0')