# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb

def getSol(N,K,P):
    dp = []
    for x in range(N+1):  
        dp.append([0]*(P+1))
    
    for x in range(N):
        dp[x+1] = dp[x][:]
        arr = list(map(int,input().split()))
        s = 0
        for y in range(K):
            s += arr[y]
            for z in range(P-y):
                dp[x+1][z+y+1] = max(dp[x][z]+s, dp[x+1][z+y+1])                
    return dp[N][P]

T = int(input())
for x in range(T):
    [N,K,P] = list(map(int,input().split()))
    mysol = getSol(N,K,P)
    print('Case #{}: {}'.format(x+1,mysol))
