T = int(input())
for t in range(T):
    N, A, B = map(int,input().split())
    arr = list(map(int,input().split()))
    A = [A,B]
    
    sons = [[] for x in range(N)]
    for i in range(N-1):
        sons[arr[i]-1].append(i+1)
    
    par = [[[] for _ in range(20)] for __ in range(N)]
    depth = [0 for _ in range(N)]
    for i in range(N-1):
        depth[i+1] = depth[arr[i]-1]+1
        par[i][0] = sons[i]
    
    for i in range(N-1,-1,-1):
        j = 0
        while 0 < len(par[i][j]):
            for k in par[i][j]:
                par[i][j+1] += par[k][j]
            j += 1

    # for i in range(2):
    #     B = A[i]
    #     l = 0
    #     while B: #O(log B)
    #         if 0 < B&(2**l):
    #             B >>= (l+1)
    #             print(l)
    #             l = 0
    #         else: 
    #             l += 1

    sons = [[None for _ in range(N) ] for __ in range(2)]
    for i in range(2):
        for j in range(N):
            curr, new = [j], []
            B = A[i]
            l = 0
            while B: #O(log B)
                if 0 < B&(2**l):
                    B -= B&(2**l)
                    for k in curr:
                        new += par[k][l]
                    curr = new
                    new = []
                else: 
                    l += 1
            sons[i][j] = curr
            
    for x in sons:
        print(x)
    print()

    ans = 0
    visits = [[1 for _ in range(N)] for __ in range(2)]
    for i in range(N-1,-1,-1):
        for j in range(2):
            for x in sons[j][i]:
                visits[j][i] += visits[j][x]
        va = visits[0][i]/N
        vb = visits[1][i]/N
        ans += va + vb - va*vb
    
    for x in visits:
        print(x)
    print()

    print('Case #{}: {}'.format(t+1,round(ans,7)))

"""
4
8 1 2
1 1 3 4 4 3 4
10 3 4
1 1 1 1 1 1 1 1 1
17 3 1
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
17 2 2
1 1 3 4 4 3 4 7 6 9 9 11 11 14 15 16 17


3
8 3 2
1 1 3 4 4 3 4
10 3 4
1 1 1 1 1 1 1 1 1
4 3 1
1 2 3
"""