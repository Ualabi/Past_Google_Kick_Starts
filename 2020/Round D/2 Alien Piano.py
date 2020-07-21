# Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387174

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    
    dp = [[float('inf') for _ in range(4)] for __ in range(N)]
    dp[0] = [0, 0, 0, 0]
    for x in range(1,N):
        if A[x] == A[x-1]:
            for y in range(4):
                dp[x][y] = dp[x-1][y]
        elif A[x-1] < A[x]:
            for y in range(4):
                minim = float('inf')
                for z in range(y):
                    minim = min(minim,dp[x-1][z])
                for z in range(y,4):
                    minim = min(minim,dp[x-1][z]+1)
                dp[x][y] = minim
        else:
            for y in range(4):
                minim = float('inf')
                for z in range(y+1):
                    minim = min(minim,dp[x-1][z]+1)
                for z in range(y+1,4):
                    minim = min(minim,dp[x-1][z])
                dp[x][y] = minim
    
    print('Case #{}: {}'.format(t+1,min(dp[-1])))