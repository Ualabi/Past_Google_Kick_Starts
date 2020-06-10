T = int(input())
for t in range(T):
    A, N, P = map(int,input().split())
    if A%P == 0:
        print('Case #{}: 0'.format(t+1))
        continue
    
    a, m = (A*A)%P, [A%P]
    while a != A%P:
        m.append(a)
        a = (a*A)%P
        if a == 0:
            m.append(0)
            break
    l = len(m)
    if l == 1:
        print('Case #{}: {}'.format(t+1,m[0]))
        continue
    m = m[-1:] + m
    
    f = 1
    for x in range(2,N+1):
        f = (f*x)%l
    
    # print(m)
    
    print('Case #{}: {}'.format(t+1,m[f]))