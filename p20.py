while True:
    x = input("press y/Y : ")
    if x == 'y' or x =='Y':
        num = int(input("please enter a num : "))
        if num== 100:
            print('num is 100')
        elif num == 1000:
            print('num is 1000')
        elif num == '2000':
            print('num is 2000')
    else:
        break