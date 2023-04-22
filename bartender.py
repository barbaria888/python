dic = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}

k = 1
l = 0
cou = 0
v_lis = list(dic.values())

for i in range(len(dic) - 1):  
    for j in range(k, len(v_lis[i])):
        if v_lis[i][j] == v_lis[i+1][j]:
            cou += 1
            k += 1
        else:
            break
    if k == len(v_lis[i]):
        l = 1
        break  

if l == 1:
    print("Number of matches:", cou)
