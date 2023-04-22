import random
n = int(input('Enter the number of times you have to play:'))
set = ['glass','iron','steel','wood']
print('Pick random object from the following:')
print(*set)
score = 0
for i in range(n):
    user = input('YOUR TURN ')
    com = random.choice(set)
    print(com)
    if com == user:
        score += 100
        
print(f'Score Is:{score}')        