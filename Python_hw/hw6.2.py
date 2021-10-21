def x(n):
    t = 0
    while n - 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2!= 0:
            n = n * 3 + 1
        t += 1
    return t

a = [x(n) for n in range(10,101)]

print('10 - 100之間的次數:')
print(a) 

print('最多為', max(a), '次')