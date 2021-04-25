# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201c09

def fun1(m,M):
    ans = [1]
    for x in range(M):
        ans.append(ans[-1]*(1+m))
        x += 1
    ans[-1] = -ans[-1]
    return ans

T = int(input())
for i in range(T):
    M = int(input())
    arr = list(map(int,input().split()))
    
    a = arr[0]
    b = sum(arr[1:])
    if a == b:
        print('Case #{}: 0.0000000'.format(i+1))
        continue

    l = -1
    r = 1
    pm = -1
    while True:
        m = (l+r)/2 
        if abs(pm-m) < 0.0000005:
            break
        
        A = fun1(m,M)
        
        suma = 0
        for x in range(M+1):
            suma += A[M-x]*arr[x]
        

        if suma == 0:
            break
        if suma > 0:
            l = m
        elif suma < 0:
            r = m
        pm = m
    print('Case #{}: {}'.format(i+1,m))