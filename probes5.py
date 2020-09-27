from math import ceil

T = int(input())
for t in range(T):
    N, K = map(int,input().split())
    intervals = []
    for n in range(N):
        aux = list(map(int,input().split()))
        intervals.append(aux)
    
    intervals.sort(key = lambda x: x[0])
    
    prv = 0
    ans = 0
    for [x,y] in intervals:
        if x < prv and prv < y:
            aux = (y-prv)//K
            if (y-prv)%K:
                aux += 1
            
            ans += aux
            prv = prv + aux*K
                
        elif prv <= x:
            aux = (y-x)//K
            if (y-x)%K:
                aux += 1
            
            ans += aux
            prv = x + aux*K
        # print('---',ans,prv)
        
    print('Case {}: {}'.format(t+1,ans))