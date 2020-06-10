# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b7d/0000000000201c03

T = int(input())
for t in range(T):
    A, N, P = map(int,input().split())
    if A%P == (A*A)%P:
        print('Case #{}: {}'.format(t+1,A%P))
        continue
    
    myset = set()
    myset.add(A%P)
    a, m = (A*A)%P, [A%P]
    while a not in myset:
        myset.add(a)
        m.append(a)
        a = (a*A)%P
    
    if m[-1] == 0:
        fl, r, f, l = True, 1, 1, len(m)
        for x in range(2,N+1):
            if fl:
                r *= x
                if r >= l:
                    fl = False
            f = (f*x)%l
            if f == 0:
                break
        if fl:
            print('Case #{}: {}'.format(t+1,m[(l+f-1)%l]))
        else:
            print('Case #{}: 0'.format(t+1))
        continue
        
    offset = m.index((m[-1]*A)%P)
    if offset:
        fl, r, f, l = True, 1, 1, len(m)-offset
        for x in range(2,N+1):
            if fl:
                r *= x
                if r >= offset:
                    fl = False
            f = (f*x)%l
            if f == 0:
                break
        if fl:
            print('Case #{}: {}'.format(t+1,m[f-1]))
        else:
            print('Case #{}: {}'.format(t+1,m[offset+(2*l+f-offset-1)%l]))
    else:
        f, l = 1, len(m)
        for x in range(2,N+1):
            f = (f*x)%l
            if f == 0:
                break
        print('Case #{}: {}'.format(t+1,m[(l+f-1)%l]))