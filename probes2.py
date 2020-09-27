import sys 
from random import randint
sys.setrecursionlimit(100000000) 

class Solution():
    def __init__(self, N, I, fathers):
        self.N = N
        self.I = I
        self.sons = [[] for x in range(self.N)]
        for i in range(N-1):
            self.sons[fathers[i]-1].append(i+1)
        self.bigsons = [[[] for _ in range(2)] for __ in range(self.N)]
        self.visits = [[1 for _ in range(2)] for __ in range(self.N)]
        self.visited = []
        self.height = 0
        self.dfs(0,0)
    
    def dfs(self,ind,height):
        print(height)
        self.visited.append(ind)
        self.dfs(ind+1,height+1)
        self.visited.pop()

    def solve(self):
        ans = 0
        for i in range(self.N-1,-1,-1):
            for j in range(2):
                for k in self.bigsons[i][j]:
                    self.visits[i][j] += self.visits[k][j]
            va = self.visits[i][0]/self.N
            vb = self.visits[i][1]/self.N
            ans += va + vb - va*vb
        return ans

def fun1(N,A,B,arr):
    I = [A,B]
    sol = Solution(N,I,arr)
    return round(sol.solve(),6)

def fun2(N,A,B,arr):
    A = [A,B]
    par = [[0 for _ in range(20)] for __ in range(N)]
    depth = [0 for _ in range(N)]
    for i in range(1,N):
        par[i][0] = arr[i-1]-1
        depth[i] = depth[par[i][0]]+1
        z = 0
        while 0 < par[i][z]:
            par[i][z+1] = par[par[i][z]][z]
            z += 1
    ans = 0
    cnt = [[0 for _ in range(2)] for __ in range(N)]
    for i in range(N-1,-1,-1):
        for z in range(2):
            cnt[i][z] += 1
            if (depth[i] < A[z]):
                continue
            cur = i
            l, v = 0, A[z]
            while 0 < v:
                if 0 < (v & 1):
                    cur = par[cur][l]
                v >>= 1
                l += 1
            cnt[cur][z] += cnt[i][z]
        va = (cnt[i][0]+0.0) / N
        vb = (cnt[i][1]+0.0) / N
        ans += va + vb - va*vb
    return round(ans,6)

flag = True
N = 50000
i = 0
while True:
    i += 1
    A = 2
    B = 3
    arr = [x+1 for x in range(N-1)]
    print(i,A,B)
    print(arr[:10])
    print(arr[-10:])
    a = fun1(N,A,B,arr)
    print(a)
    
    
    b = fun2(N,A,B,arr)
    print(b)
    
    flag = False
    # flag = a==b