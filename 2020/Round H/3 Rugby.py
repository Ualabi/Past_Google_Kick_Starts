# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b027

T = int(input())
for t in range(T):
    N = int(input())
    N2 = N//2
    
    X, Y = [], []
    for n in range(N):
        x,y = map(int, input().split())
        Y.append(y)
        X.append(x)
    Y.sort()
    X.sort()
    for i in range(N): X[i] -= i
    X.sort()
    mx = X[N2]
    my = Y[N2]
    
    ans = 0
    for x in X: ans += abs(x - mx)
    for y in Y: ans += abs(y - my)
    print('Case #{}: {}'.format(t+1,ans))