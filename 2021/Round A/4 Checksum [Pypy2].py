# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3

T = int(input())
for t in range(T):
    N = int(input())
    A, B, Z = [], [], []
    for n in range(N):
        A.append(list(map(int,raw_input().split())))
    for n in range(N):
        B.append(list(map(int,raw_input().split())))
    Z = raw_input()
    Z = raw_input()

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
        grafo[n].sort(key = lambda x: x[0])

    # Count the value of the edges of the Maximum Weight Spanning Forest
    cnt = 0
    gn = nodes.count(True)
    index = [len(grafo[n])-1 for n in range(2*N)]
    while gn:   # While some nodes to check
        mxnod = nodes.index(True)
        nodes[mxnod] = False
        taken = {mxnod}
        minim = set()
        gn -= 1
        
        # While the taken != the ones with max index reached
        while len(taken) != len(minim):
            mxcst, mxnod = 0, None
            for n in taken-minim:
                while 0 <= index[n] and grafo[n][index[n]][1] in taken:
                    index[n] -= 1
                if index[n] < 0:
                    minim.add(n)
                elif mxcst < grafo[n][index[n]][0]:
                    mxcst = grafo[n][index[n]][0]
                    mxnod = grafo[n][index[n]][1]
                    visit = n
            if mxnod is None:
                break

            index[visit] -= 1
            nodes[mxnod] = False
            taken.add(mxnod)
            cnt += mxcst
            gn -= 1
            
    print('Case #{}: {}'.format(t+1,total-cnt))