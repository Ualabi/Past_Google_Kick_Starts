# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff4/0000000000051183

def solve(N):
    a = 0
    for i in range(N-N%10,N+1):
        if "9" not in str(i) and i%9 != 0:
            a += 1
    N -= N%10
    b, m = 0, 1
    while N:
        b += (N%10)*m
        m *= 9
        N = N//10
    return a +  8 * b//9

T = int(input())
for t in range(T):
    F, L = map(int,input().split())
    ans = solve(L) - solve(F) + 1
    print('Case #{}: {}'.format(t+1,ans))