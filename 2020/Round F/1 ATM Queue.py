# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4ed8

T = int(input())
for t in range(T):
    N, X = map(int,input().split())
    arr = list(map(int,input().split()))
    
    queue = []
    for n in range(N):
        times = arr[n]//X
        if arr[n]%X:
            times += 1
        queue.append([times, n+1])
    
    outs = ''
    ax = sorted(queue, key=lambda x: x[0])
    for x, y in ax:
        outs += '{} '.format(y)
    
    print('Case #{}: {}'.format(t+1,outs))