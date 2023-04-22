from math import sqrt
x1 = int(input('enter the x coordinate'))
y1 = int(input('enter the y coordinate'))
z1 = int(input('enter the z coordinate'))
x2 = int(input('enter the x coordinate'))
y2 = int(input('enter the y coordinate'))
z2 = int(input('enter the z coordinate'))
 
re = (z2-z1)**2 + (y2-y1)**2 + (x2-x1)**2
d = sqrt(re)
print(d)