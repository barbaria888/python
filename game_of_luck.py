import random
n = int(input('How many times would you be able to play? '))
computer = random.randint(1,n)
score = 0
for i in range(n):
    entry = int(input('ENTER YOUR GUESS:'))
    if entry == computer:
        print('CONGRATULATIONS YOU WON!')
        score += 100 
    else:
        print('SORRY,PLEASE TRY AGAIN...')
        score -= 10
print(f'Your Score is: {score}')
if score >= 50:
    print('YOU ARE LUCKY TODAY')