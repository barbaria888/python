A = int(input('enter the initial value '))
B = int(input('enter the final value'))
for i in range(A,B):
    if i % 2 == 0 or i % 3 ==0 or i % 5 == 0: 
        if i == 2 or i == 3 or i == 5:
            print('please enter a number except 0,1,2,3')
    else:
        print(f'the prime numbers are{i}')
      
        