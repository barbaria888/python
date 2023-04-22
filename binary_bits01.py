''' task is, you will be given 2 integers and a thershold k. find the maximum value between bitwise and, or and xor. the maximum should not greater than the thershold k.

default maximum value is zero.'''
x,y =input().split()
a=int(x)
b=int(y)
k=int(input())
#operations
xor = a^b
anD = a and b
oR = a or b
#comparing
best = max(xor,max(anD,oR))
higher = 0
if best <= k:
  higher=best
'''ans = max(best,k)'''  
print(higher)
  