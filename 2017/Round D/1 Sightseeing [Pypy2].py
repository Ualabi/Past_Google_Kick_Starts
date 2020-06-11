# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b77/0000000000201bfd
# Use PyPy2 to run it, it does not pass the TLE with Python 3/2

inf = float('inf')
T = int(input())
for t in range(T):
    N, Ts, Tf = map(int,raw_input().split())
    D = [[inf for _ in range(N)] for __ in range(N)]
    for x in range(N-1):
        W, P, V = map(int,raw_input().split())
        if x == 0:
            D[1][0] = W + V
            D[1][1] = max(Ts,W) + (P-(Ts-min(Ts,W))%P)%P + V
        else:
            for y in range(x+2):
                if y == 0:      #Ciudad x con vistas 0
                    Ac = D[x][0]
                    m = max(Ac,W) + (P-(Ac-min(Ac,W))%P)%P + V
                elif y == x+1:  #Ciudad x con vistas x
                    Ac = D[x][y-1]
                    m = max(Ac+Ts,W) + (P-(Ac+Ts-min(Ac+Ts,W))%P)%P + V
                else:           #Ciudad x con vistas y
                    Al = D[x][y-1]
                    l = max(Al+Ts,W) + (P-(Al+Ts-min(Al+Ts,W))%P)%P + V
                    
                    Ar = D[x][y]
                    r = max(Ar,W) + (P-(Ar-min(Ar,W))%P)%P + V
                    
                    m = min(l,r)
                
                if m <= Tf:
                    D[x+1][y] = m
                else:
                    break
    
    maxim = -1
    for x in range(N):
        if D[N-1][x] <= Tf:
            maxim = x
        else:
            break
        
    ans = maxim if maxim >= 0 else 'IMPOSSIBLE'
    print('Case #{}: {}'.format(t+1,ans))