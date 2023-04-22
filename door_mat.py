c = '*|*'
w = 'WELCOME'
m = int(input('enter the size'))
for i in range(m//2):
    print('-' * ((3 * m - ( 2 * i + 1)) // 2), c * (2 * i + 1), '-'*(((3 * m - (2 * i + 1 )))//2),sep='')
print('-'*((3*m-7) // 2 ),w,'-'*((3 * m - 7) // 2))

for i in range(m//2,-1,-1):
    print('-' * ((3 * m - ( 2 * i + 1)) // 2), c * (2 * i + 1), '-' * (((3 * m - (2 * i + 1))) // 2),sep='')