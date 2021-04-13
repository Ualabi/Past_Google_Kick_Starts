# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b027

T = int(input())
for t in range(T):
    N = int(input())
    if N > 10:
        exit()
    
    X, Y = [], []
    for n in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    
    miny = float('inf')
    for y in range(-510,510):
        aux = 0
        for yy in Y:
            aux += abs(y-yy)
        miny = min(miny,aux)
    
    minx = float('inf')
    for x in range(-510,500):
        aux = 0
        for i,xx in enumerate(X):
            aux += abs(x+i-xx)
        minx = min(minx,aux)
    
    ans = miny+minx
    print('Case #{}: {}'.format(t+1,ans))