T = int(input())
for i in range(T):
    N = int(input())
    arr = {}
    for ii in range(N):
        aux = input()
        l = len(set(aux.replace(' ','')))
        arr[l] = arr.get(l,[]) + [aux]
    
    maxim = sorted(arr)[-1]
    print('Case #{}: {}'.format(i+1, sorted(arr[maxim])[0]))