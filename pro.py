lim = 10**9
primes = [3,5,7]

vals = []
for prime in primes:
    aux = []
    val = 1
    while val*prime <= lim:
        val *= prime
        aux.append(val)
    vals.append(aux)

allvals = []
for x,y in [(0,1),(0,2),(1,2)]:
    for i in vals[x]:
        for j in vals[y]:
            val = i+j
            if val <= lim:
                allvals.append(val)
allvals.sort()

T = int(input())
for t in range(T):
    N = int(input())
    I = int(input())
    D = int(input())

    if N <= 3+5:
        print( (8-N)*I ) 
        continue

    l,r = 0, len(allvals)
    while l<r:
        m = (l+r)//2
        if allvals[m] <= N:
            l = m+1
        else:
            r = m
    
    minim = float('inf')
    for i in [-1,0,1]:
        ni = r+i
        if 0<=ni and ni < len(allvals):
            if allvals[ni] <= N:
                minim = min(minim, D*(N-allvals[ni]))
            else:
                minim = min(minim, I*(allvals[ni]-N))

    print( minim )
