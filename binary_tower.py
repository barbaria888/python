n= int(input())
num = 0
st=''
for i in range(n):
    for j in range(i):
        print(' '*(j+1),end='')
    for j in range(i,-1,-1):
        st = str(num)
        num = bin(eval(st) + i)
        print(st)
    