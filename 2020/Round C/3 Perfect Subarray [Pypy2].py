# Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003381cb

squares = []
for x in range(1,int((100*100000)**0.5)+1):
    squares.append(x*x)

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int,raw_input().split()))
    m = max(arr)
    
    ans = 0
    suma = 0
    freq = {}
    for x in range(N):
        suma += arr[x]
        freq[suma] = freq.get(suma,0) + 1
        
        if suma == 0: #to sum up 0
            ans += freq.get(suma,0)
        else:
            ans += freq.get(suma,1)-1
        
        for y in squares:
            if suma == y: # suma == square
                ans += 1 + freq.get(0,0)
            elif (suma-y) in freq: # suma - subarr == square
                ans += freq[suma-y]
            if m*(x+1) < y:
                break
    
    print('Case #{}: {}'.format(t+1,ans))