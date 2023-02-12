amt = int(input('enter the amount'))
temp = amt-100

tt = temp//2000
temp%=2000
fh = temp//500
temp %= 500
th = temp//200
temp %= 200
hun = (temp//100) + 1

print('the amount %d contains\n %d two thousand rupee notes\n %d fivehundred rupee notes \n%d two hundred rupee notes\n %d hundred rupee notes '%(amt,tt,fh,tt,hun))