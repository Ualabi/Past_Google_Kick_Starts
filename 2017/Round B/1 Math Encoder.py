# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d27/0000000000201b7b

m = 1000000007
pots = [1]
for x in range(10000):
    n = (pots[-1]*2)%m
    pots.append(n)

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for n in range(N):
        aux = A[n]*(pots[n] - pots[N-n-1])
        ans = (ans + aux)%m
    
    print('Case #{}: {}'.format(t+1,(ans+m)%m))