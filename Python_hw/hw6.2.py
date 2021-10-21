num = int(input('輸入一個數字'))

while num >= 1:
    if num%2 == 1:
        num = num*3+1
        print(num)
    else:
        num = num/2
        print(num)