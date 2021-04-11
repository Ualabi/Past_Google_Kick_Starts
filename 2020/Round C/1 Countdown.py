# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2

T = int(input())
for t in range(T):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    
    ans = 0
    val = K
    for x in arr:
        if x == K:
            val = K-1
        elif x == val:
            if val == 1:
                ans += 1
                val = K
            else:
                val -= 1
        elif val < K:
            val = K
            
    print('Case #{}: {}'.format(t+1,ans))