# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24

T = int(input())
for t in range(T):
    W, N = map(int,input().split())
    X = list(map(int,input().split()))
    
    X.sort()
    M = W//2
    ans = sum( [abs(X[M]-x) for x in X])
    cur = ans
    if W <= 1:
        print('Case #{}: {}'.format(t+1,ans))
        continue
        
    for i in range(W):
        M1 = (M+1) % W
        if M1 < W//2:
            X[M1] += N
        if W % 2 == 0:
            cur += X[M1] - X[M]
        cur += ( X[i] + N - X[M1] ) -  (X[M] - X[i])
        ans = min(cur,ans)
        M = M1

    print('Case #{}: {}'.format(t+1,ans))