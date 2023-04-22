import math
x = int(input('enter the X coordinate of center'))
y = int(input('enter the Y coordinate of center'))
rad = int(input('enter the radius of circle'))
px = int(input('enter the points X coordinate'))
py = int(input('enter the points Y coordinate'))
 #logic
temp = (px*px) + (py*py)
dist = math.sqrt(temp) 
 
if dist <= rad :
    print('yes, given points %d and %d lie inside the circle'%(px,py))
else:
    print('no,given points  %d and %d doesntlie inside the circle'%(px,py))