# main_code
n = int(input())
c = 0    
s = -1   

while s != 6174:
    x = ''.join(sorted(str(n).zfill(4)))  # Sort the digits in ascending order, padding with leading zeros if necessary
    y = x[::-1]  
    x, y = int(x), int(y)  
    s = abs(x - y)  
    n = s  
    c += 1

print("Number of iterations to reach 6174:", c)
