#_main_




def subarraysum():
    
    inp = list((input('enter the elements')))
    arr=[]
    n=len(arr)
    s = int(input('enter the sum of the elements'))
    som = 0
    ind1 = 0
    ind2 = 0
    for i in range(n):
        som += arr[i]
        if som == s:
            ind1 = i
            for j in range(ind1,-1,-1):
                if som == s:
                    ind1 = j
                    print(ind1)
                    print(ind2)
                else:
                    arr[i]=arr[-1]
                    print(arr)

subarraysum()