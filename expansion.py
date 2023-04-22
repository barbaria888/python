def factorial(x):
    out=1
    for i in range(1,x+1):
        out *=i
    return out 
    
n = int(input())
k=0
c=1
x= 0
out =0
while k!=n:
    x = c**k
    out += x/factorial(k)
    k+=1
    print(f'x^{k}/{k}! +',end='')
print()
print('=',end='')
print(out)
