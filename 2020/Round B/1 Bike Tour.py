# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6

T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for x in range(1,N-1):
        if arr[x-1] < arr[x] and arr[x] > arr[x+1]:
            count += 1
    
    print('Case #{}: {}'.format(i+1,count))
