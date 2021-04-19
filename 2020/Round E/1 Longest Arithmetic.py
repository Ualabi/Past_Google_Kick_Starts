# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bf4ed

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    
    cnt = 2
    i, maxim = 2, 2
    past = A[1]-A[0]
    while i < N:
        curr = A[i]-A[i-1]
        if curr == past:
            cnt += 1
            if cnt > maxim:
                maxim = cnt
        else:
            cnt = 2
        past = curr
        i += 1
        
    print('Case #{}: {}'.format(t+1, maxim))