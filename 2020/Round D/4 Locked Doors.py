# Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386d5c

T = int(input())
for t in range(T):
    N, Q = map(int,input().split())
    D = list(map(int,input().split()))
    head = max(D)

    i = {}
    for x,d in enumerate(D): i[d] = x

    LS, LI, RS, RI = [], [], [], []
    for x in range(N-1):
        while (LS and LS[-1]<D[x]): LS.pop()
        if not LS: LI.append(-1)
        else: LI.append(LS[-1])
        LS.append(D[x])
        while (RS and RS[-1]<D[N-2-x]): RS.pop()
        if not RS: RI.append(-1)
        else: RI.append(RS[-1])
        RS.append(D[N-2-x])
    RS.reverse()
    RI.reverse()
    # print(LS, LI, RS, RI)

    LP, RP = [-1]*(N-1), [-1]*(N-1)
    for x in range(N-1):
        if 0 < LI[x]: LP[i[LI[x]]] = max(LP[i[LI[x]]], D[x])
        if 0 < RI[x]: RP[i[RI[x]]] = max(RP[i[RI[x]]], D[x])
    # print(LP, RP)

    PT, LC, RC = [-1]*(N-1), [-1]*(N-1), [-1]*(N-1)
    for x in range(N-1):
        if 0 < LP[x]:
            RC[x] = LP[x]
            PT[i[LP[x]]] = D[x]
        if 0 < RP[x]:
            LC[x] = RP[x]
            PT[i[RP[x]]] = D[x]    
    # print(PT, LC, RC)

    vals, queue = [], [head]
    while queue:
        nqueue = []
        for q in queue:
            vals.append(q)
            if 0 < LC[i[q]]:
                nqueue.append(LC[i[q]])
            if 0 < RC[i[q]]:
                nqueue.append(RC[i[q]])
        queue = nqueue
    # print(vals)

    SM = [1]*(N-1)
    stack = vals[::]
    while stack:
        n = stack.pop()
        if 0 < LP[i[n]]: SM[i[n]] += SM[i[LP[i[n]]]]
        if 0 < RP[i[n]]: SM[i[n]] += SM[i[RP[i[n]]]]
    # print(SM)

    l = []
    for n in range(N-1):
        if 0 < PT[n]:
            l.append([D[n], PT[n]])
        else:
            l.append([D[n]])
    # print(l)

    x = 1
    nxt = True
    while nxt:
        nvals = []
        nxt = False
        for v in vals:
            if x == len(l[i[v]])-1:
                y = l[i[v]][x]
                if x <= len(l[i[y]])-1:
                    nxt = True
                    z = l[i[y]][x]
                    nvals.append(v)
                    l[i[v]].append(z)
        vals = nvals
        x += 1
    # print(l)
    
    ans = []
    for q in range(Q):
        S, K = map(int,input().split())

        if K == 1:
            ans.append(S)
            continue
        if S == 1:
            ans.append(S+K-1)
            continue
        if S == N:
            ans.append(S-K+1)
            continue
        if D[S-2] < D[S-1] and K-1 <= SM[S-2]:
            ans.append(S-K+1)
            continue
        if D[S-1] < D[S-2] and K-1 <= SM[S-1]:
            ans.append(S+K-1)
            continue

        S, K = S-1, K-1
        L, R = min(D[S-1], D[S]), max(D[S-1], D[S])
        
        j = i[L]
        x = len(l[j])-1
        while 0 < x:
            # print(K, j, SM[i[l[j][x]]], l[j], x, l[j][x])
            if K < SM[i[l[j][x]]]:
                x -= 1
            elif K > SM[i[l[j][x]]]:
                j = i[l[j][x]]
                if len(l[j]) <= x:
                    x = len(l[j])-1
            else:
                j = i[l[j][x]]
                x = 0
        
        if SM[j] < K:
            j = i[l[j][1]]

        if 0 < LC[j] and 0 < RC[j]:
            if j < S: 
                ans.append(j + 2 + SM[i[RC[j]]] - K)    
            else:
                ans.append(j + 1 - SM[i[LC[j]]] + K)
        elif 0 < LC[j]:
            ans.append(j + 2 - SM[j] + K)
        elif 0 < RC[j]:
            ans.append(j + 1 + SM[j] - K)
        else:
            # Error
            ans.append(S)
  
    print("Case #{}: {}\n".format(t+1, ' '.join(map(str,ans))))