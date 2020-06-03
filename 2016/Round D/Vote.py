# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201db8/0000000000201c06

lim = 2001
dp = [[0 for _ in range(lim)] for __ in range(lim)]
for c in range(lim):
    dp[0][c] = 1
for c in range(1,lim):
    for r in range(1,c):
        dp[r][c] = dp[r][c-1]*(c/(r+c)) + dp[r-1][c]*(r/(r+c))

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    print('Case #{}: {}'.format(t+1,dp[M][N]))