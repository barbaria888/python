l = 5 #int(input())
b = 5 #int(input())
for i in range(1,l+1):
    for j in range(1,b+1):
        print('*',end='')
        if j== (l - 2 ):
            print(' '*(j+1),end='')
        if i == (b - 2):
            print(' '*(i+1),end='')

        if j == (b//2) and (i != 1 or i != l) :
            pass
    print()        