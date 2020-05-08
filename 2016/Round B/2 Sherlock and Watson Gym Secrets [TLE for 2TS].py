# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c0c/0000000000201d32
# This algoritgm didnt pass the TLE for the second test set in python 3, but it did in c++, thats why I attached both solutions

def exp(x,A,B,K):
    if K == 1:
        return 0, 0
    a, b = 1, 1
    aux = x
    while A or B:
        if aux == 0:
            if A:   a = 0
            if B:   b = 0
            break
        if A%2 == 1:
            a = (a*aux)%K
        if B%2 == 1:
            b = (b*aux)%K
        aux = (aux*aux)%K
        A = A//2
        B = B//2
    return a,b

l = 10**9 + 7
T = int(input())
for _ in range(T):
    A, B, N, K = map(int,input().split())
    a, b = {}, {}
    count = 0
    for x in range(1,min(N+1,K+1)):
        cnt = ((N-x)//K + 1) % l
        i,j = exp(x,A,B,K)
        a[i] = a.get(i,0)+cnt
        b[j] = b.get(j,0)+cnt
        if (i+j)%K == 0:
            count += cnt
            count %= l
    suma = 0
    for x in a:
        y = (K-x)%K
        if y in b:
            suma += (a[x]%l * b[y]%l)%l
            suma %= l
    print('Case #{}: {}'.format(_+1,(suma+l-count)%l))
