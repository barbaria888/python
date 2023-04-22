a = [64,100]#given array(of coins)
a.sort() #sorting the list
f = 1 #flag
numop =0 #no. of pockets
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        f += 1
        if  f % i == 0:
            numop += f // i 
print(numop)
