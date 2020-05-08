# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf

T = int(input())
for i in range(T):
    N, D = map(int,input().split())
    arr = list(map(int,input().split()))
    for x in range(N-1,-1,-1):
        D -= D%arr[x]
                
    print('Case #{}: {}'.format(i+1,D))
