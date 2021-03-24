# Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4b8b

T = int(input())
for t in range(T):
    N, K = map(int,input().split())
    intervals = []
    for n in range(N):
        aux = list(map(int,input().split()))
        intervals.append(aux)
    
    intervals.sort(key = lambda x: x[0])
    
    ans, prv = 0, 0
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
        
    print('Case #{}: {}'.format(t+1,ans))