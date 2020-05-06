# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201ca3

T = int(input())
for i in range(T):
    ans = 0
    M, N = map(int,input().split())
    A = {}
    for x in N:
        B = list(map(int,input().split()))
        C = list(map(int,input().split()))
        D = list(map(int,input().split()))
        A[x] = [B,C,D]
    
    
    
    print('Case #{}: {}'.format(i+1,ans))