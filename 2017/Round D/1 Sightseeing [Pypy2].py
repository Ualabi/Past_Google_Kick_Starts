# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b77/0000000000201bfd
# Even though I coded it as efficient as I can with O(N) <= bigO <= O(N^2)
# It does not pass the TLE with PyPy2 for the second test set, as they put 20 seconds per test set
# In this program is mandatory to use C++

inf = float('inf')
T = int(input())
for t in range(T):
    N, Ts, Tf = map(int,raw_input().split())
    for x in range(N-1):
        W, P, V = map(int,raw_input().split())
        if x == 0:
            D = {
                (1,0) : W + V,
                (1,1) : max(Ts,W) + (P-(Ts-min(Ts,W))%P)%P + V
            }
        else:
            for y in range(x+2):
                if (x,y-1) in D:
                    Al = D[x,y-1]
                    l = max(Al+Ts,W) + (P-(Al+Ts-min(Al+Ts,W))%P)%P + V
                else:
                    l = inf
                if (x,y) in D:
                    Ar = D[x,y]
                    r = max(Ar,W) + (P-(Ar-min(Ar,W))%P)%P + V
                else:
                    r = inf
                
                m = min(l,r)
                if m <= Tf:
                    D[x+1,y] = m
                else:
                    break
    
    maxim = -1
    for x in range(N):
        if (N-1,x) in D:
            if D[N-1,x] <= Tf:
                maxim = x
            else:
                break
        else:
            break
        
    ans = maxim if maxim >= 0 else 'IMPOSSIBLE'
    print('Case #{}: {}'.format(t+1,ans))