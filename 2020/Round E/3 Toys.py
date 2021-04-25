# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bede9#problem

from heapq import heappop, heappush

T = int(input())
for t in range(T):
    N = int(input())
    
    arr = []
    time = 0
    for n in range(N):
        a, b = map(int, input().split())
        arr.append([a,b])
        time += a
    
    heap = []
    curr, maxi, rmv, cnt = 0, 0, 0, 0
    for n in range(N):
        a,b = arr[n]
        if a+b > curr+time:
            if maxi < 2*curr+time:
                maxi = 2*curr+time
                cnt = rmv
            rmv += 1
            time -= a
            while heap and curr+time < -heap[0][0]:
                c,d = heappop(heap)
                curr -= d
                rmv += 1
        else:
            time -= a
            curr += a
            heappush(heap,(-a-b,a))

    if heap:
        print("Case #{}: {} INDEFINITELY".format(t+1, N-len(heap)))
    else:
        print("Case #{}: {} {}".format(t+1, cnt, maxi))