# Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4ed8
from heapq import heappush, heappop

T = int(input())
for t in range(T):
    N, X = map(int,input().split())
    arr = list(map(int,input().split()))
    
    heap1 = []
    queue = {}
    for n in range(N):
        if arr[n]%X:
            times = arr[n]//X + 1
        else:
            times = arr[n]//X
        
        heappush(heap1,times)
        
        if times in queue:
            heap2 = queue[times]
            heappush(heap2,n+1)
            queue[times] = heap2
        else:
            queue[times] = [n+1]
    
    outs = ''
    while heap1:
        h1 = heappop(heap1)
        heap2 = queue[h1]
        while heap2:
            h2 = heappop(heap2)
            outs += str(h2) + ' '
    
    print('Case #{}: {}'.format(t+1,outs[:-1]))