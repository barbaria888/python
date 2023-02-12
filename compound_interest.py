p = float(input('enter the principal amount'))
r = float(input('enter the rate of interest'))
n = int(input('enter the time period of one cycle(in months)'))
t = int(input('enter the no.of cycles'))
amt = p*(( 1 + r/n ))**(n*t)
CI = amt - p
print('the total amount to be paid is',amt)
print('the total interest to be paid is',CI)