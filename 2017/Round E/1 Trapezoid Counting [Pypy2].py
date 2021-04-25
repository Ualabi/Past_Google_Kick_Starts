# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201bfe/0000000000201d24
# Use PyPy2 to run it, it does not pass the TLE with Python 3/2

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,raw_input().split()))
    
    freq = {}
    for a in A:
        freq[a] = freq.get(a,0) + 1
    
    val = sorted(freq)
    lim = len(val)
        
    past = 0    
    suma = {}
    for f in val:
        past += freq[f]
        suma[f] = past
        
    ans = 0
    for a in range(lim):
        f = freq[val[a]]
        if 2 <= f:
            if 3 <= f:
                l, r = a, lim-1
                while l <= r:
                    k = (l+r)//2
                    if val[k] < 3*val[a]:
                        l = k+1
                    else:
                        r = k-1
                x = suma[val[r]] - f
                p = (f*(f-1)*(f-2))//6
                ans += x*p
            
            x = 0
            for b in range(lim-1):
                if b != a:
                    y = freq[val[b]]
                    l, r = b, lim-1
                    while l <= r:
                        k = (l+r)//2
                        if val[k] < val[b] + 2*val[a]:
                            l = k+1
                        else:
                            r = k-1
                    z = suma[val[r]] - suma[val[b]]
                    o = -f if b < a and a <= r else 0
                    z += o
                    x += y*z
            p = (f*(f-1))//2
            ans += x*p

    print('Case #{}: {}'.format(t+1,ans))