# Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bf4ed

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    
    B = []
    for i in range(1,N):
        B.append(A[i]-A[i-1])

    maxim, cnt = 2, 2
    past = B[0]
    for x in B[1:]:
        if x == past:
            cnt += 1
        else:
            if cnt > maxim:
                maxim = cnt
            cnt = 2
        past = x
        
    print('Case #{}: {}'.format(t+1,max(maxim,cnt)))