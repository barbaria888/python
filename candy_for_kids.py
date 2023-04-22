N = int(input())  #total kids
C = int(input())  #total candies available
A = 1             #each kid atleast gets
sum = 0
for i in range(1,N):
    sum += A*i 
    
if sum <= C:
  print('YES')
else:
    print('NO')