# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d29/0000000000201d2a

import sys 
sys.setrecursionlimit(10**6) 

dp = {0:0}
def solve(N):
    if N in dp:
        return dp[N]
    dp[N] = float('inf')
    for i in range(1,int(N**.5)+1):
        dp[N] = min(dp[N], solve(N - i*i) + 1)
    return dp[N]

T = int(input())
for t in range(T):
    print('Case #{}: {}'.format(t+1,solve(int(input()))))