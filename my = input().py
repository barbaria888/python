my = input()
k= 0
ls = list(my)
for i in range(0,len(my)):
    if ls[i] == ls[i+1]:
        k+=1
        temp = ls[i]
        ls[i+1]=temp
        temp = ls[i]
print(ls)        
if k == len(my):
    print('TRUE')
else:
    print('FALSE')