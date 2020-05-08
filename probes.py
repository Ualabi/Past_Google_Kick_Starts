def exp(x,A,K):
    ans = 1
    for i in range(A):
        ans = (ans*x)%K
        if ans == 0:
            return 0
    return ans

def solve(A,B,N,K):
    l = 1000000007
    a, b = {}, {}
    for x in range(1,N+1):
        i = exp(x,A,K)
        a[i] = a.get(i,0)+1
        
        j = exp(x,B,K)
        if i == 0:
            if j != 0:
                b[j] = b.get(j,0)+1
        elif j != K-i:
            b[j] = b.get(j,0)+1
    print(a)
    print(b)
    suma = 0
    for x in b:
        if K-x in a:
            suma = (suma + b[x]*a[K-x])%l
    return suma

T = int(input())
for i in range(T):
    A, B, N, K = map(int,input().split())
    ans = solve(A,B,N,K)
    print('Case #{}: {}'.format(i+1,ans))
    