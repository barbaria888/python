n = eval(input())
s =0
while s==0:
    count=0
    for i in range(0,len(n)-1):
            b=n[i]
            a=n[i+1]
            if b!=a:
                n[i]= 'R' if (b=='G'and a=='B') or(a=='G'and b=='B') else 'G' if (b=='R'and a=='B') or(b=='B'and a=='R') else 'B'
                count=1
                break
    if count==0:
        s=1
        break
print(f'"{n[0]}"')