import random
k=0
m=0
n = random.randint(1,9)
for i in range(1,9):
 if n % i == 0:
     f=1
     m=i
 elif n % i == 1:
  k = 1
  n = i
 
if k ==1:
    print(m,n)
if f== 1:
 print(m,n)