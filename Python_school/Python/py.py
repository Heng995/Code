x = 0
while x < 4:
    if x % 4 == 0:
        print("party")
    elif x - 2 == 0:
        print("cake")
    elif x / 3 == 0:
        print("greeting")
    else:
        print("birthday")
    x = x + 1
    
alist = [0, 1, 2, 3, 4]
print(0 in alist)

alist = [1,2,3,4]
blist = ['a','b','c','d']
alist = blist
print(alist )
print(blist)