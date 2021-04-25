# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a3a5

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if N <= 3:
        if N == 3 and (A[2]-A[0])%2 == 0:
            print('Case #{}: {}'.format(t+1, 3))
            continue
        else:
            print('Case #{}: {}'.format(t+1, 2))
            continue
    
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
    
    # Case the change at the border or no changes at all
    if maxim >= N-1:
        print('Case #{}: {}'.format(t+1, N))
        continue
    
    chg = 0
    l,m,r = 0,1,2
    while m < N-1:
        if (A[r]-A[l])%2 == 0:
            past = A[m]
            curr = (A[r]+A[l])//2
            A[m] = curr
            
            slp = (A[r]-A[l])//2
            
            while(r < N and A[r]-A[r-1] == slp):
                r += 1
            
            while(0 <= l and A[l+1]-A[l] == slp):
                l -= 1
            
            chg = max(chg, r-l-1)
            A[m] = past
            
            if r <= m+2:
                l,m,r = m, m+1, m+2
            else:
                l,m,r = r-1, r, r+1
            
        else:
            l,m,r = l+1, m+1, r+1
        
    print('Case #{}: {}'.format(t+1, max(chg, maxim+1)))