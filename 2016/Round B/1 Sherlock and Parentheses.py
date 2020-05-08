# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c0c/0000000000201ca5

T = int(input())
for i in range(T):
    L, R = map(int,input().split())
    m = min(L,R)
    ans = m*(m+1)//2
    print('Case #{}: {}'.format(i+1,ans))