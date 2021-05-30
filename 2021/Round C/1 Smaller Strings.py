# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e

mod = 10**9 + 7

T = int(input())
for t in range(T):
    N, K = map(int,input().split())
    S = input()
    
    M = (N-1)//2
    aux = [1]
    for x in range(M):
        aux.append( (aux[-1]*K)%mod )
    
    i = 0
    ans = 0
    while aux:
        ans += (ord(S[i]) - 97) * aux.pop()
        i += 1
    
    a = S[:N//2]
    b = S[:(N+1)//2] + a[::-1]
    
    if b < S:
        ans += 1
    
    print('Case #{}: {}'.format(t+1,ans%mod))