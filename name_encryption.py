name = input()
new = ""
for i in range(len(name)):
    new += chr(ord(name[i])- 10)
    
print(new)