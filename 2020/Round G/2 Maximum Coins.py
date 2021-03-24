# Link: https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a23

T = int(input())
for t in range(T):
    N = int(input())
    A = [0 for _ in range(2*N-1)]
    for n in range(N):
        aux = list(map(int,input().split()))
        for a in range(N):
            A[N-n+a-1] += aux[a]
    print('Case #{}: {}'.format(t+1,max(A)))