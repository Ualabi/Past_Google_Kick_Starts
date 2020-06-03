lim = 11
dp = [[0 for _ in range(lim)] for __ in range(lim)]
for c in range(lim):
    dp[0][c] = 1

for c in range(1,lim):
    for r in range(1,c):
        dp[r][c] = dp[r][c-1] * (c/(r+c)) + dp[r-1][c] * (r/(r+c))

for x in dp:
    for y in x:
        print(round(y,6),end=',')
    print()

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    if M == 0:
        print('Case #{}: 1.000000000'.format(t+1))
        continue
    elif N == 2:
        print('Case #{}: 0.333333333'.format(t+1))
        continue
    
    print('Case #{}: {}'.format(t+1,dp[M][N]))