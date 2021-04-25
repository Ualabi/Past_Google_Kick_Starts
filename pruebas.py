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
    curr, maxi = 0, 0
    for n in range(N):
        a,b = arr[n]
        
        if a+b > curr+time:
            maxi = max(maxi, 2*curr+time)
            
            time -= a
            while heap and curr+time < -heap[0][0]:
                c,d = heappop(heap)
                curr -= d
        else:
            time -= a
            curr += a
            heappush(heap,(-a-b,a))
        print(heap)
    if heap:
        print("Case #{}: INDEFINITELY".format(t+1))
    else:
        print("Case #{}: {}".format(t+1, maxi))
    
    