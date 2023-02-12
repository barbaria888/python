import math
base = float(input('enter the base'))
per =  float(input('enter the perpendicular'))

hyp = (base**2) + (per**2)
temp = math.sqrt(hyp)
print('the hypotenuse is',temp)
