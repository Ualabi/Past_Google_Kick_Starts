# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3

T = int(input())
for t in range(T):
    N = int(input())
    A, B, Z = [], [], []
    for n in range(N):
        A.append(list(map(int,input().split())))
    for n in range(N):
        B.append(list(map(int,input().split())))
    Z = input()
    Z = input()

    # Build the graph model
    total = 0
    grafo = [[] for n in range(2*N)]
    nodes = [False for n in range(2*N)]
    for r in range(N):
        for c in range(N):
            if A[r][c] == -1:
                total += B[r][c]
                nodes[r] = True
                nodes[N+c] = True
                grafo[r].append([B[r][c],N+c])
                grafo[N+c].append([B[r][c],r])
    for n in range(2*N):
        grafo[n].sort(key=lambda x: x[0], reverse=True)

    # Count the value of the edges of the Maximum Weight Spanning Forest
    cnt = 0
    gn = nodes.count(True)
    index = [0 for n in range(2*N)]
    while gn:
        mxnod = nodes.index(True)
        nodes[mxnod] = False
        taken = {mxnod}
        maxim = set()
        gn -= 1
        
        while len(taken) != len(maxim):
            mxcst, mxnod = 0, None
            for n in taken-maxim:
                while index[n] < len(grafo[n]) and grafo[n][index[n]][1] in taken:
                    index[n] += 1
                if len(grafo[n]) == index[n]:
                    maxim.add(n)
                elif mxcst < grafo[n][index[n]][0]:
                    mxcst = grafo[n][index[n]][0]
                    mxnod = grafo[n][index[n]][1]
                    visit = n
            if mxnod is None:
                break

            index[visit] += 1
            nodes[mxnod] = False
            taken.add(mxnod)
            cnt += mxcst
            gn -= 1
            
    print('Case #{}: {}'.format(t+1,total-cnt))