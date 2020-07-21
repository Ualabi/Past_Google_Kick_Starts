# Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387171

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    
    ans = 0
    maxim = float('-inf')
    for x in range(N):
        if x == N-1:
            if arr[x] > maxim:
                ans += 1
                maxim = arr[x]
        else:
            if arr[x] > maxim and arr[x] > arr[x+1]:
                ans += 1
                maxim = arr[x]
            if maxim  == float('-inf'):
                maxim = arr[0] 
    
    print('Case #{}: {}'.format(t+1,ans))