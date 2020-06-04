# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201ca3
class Solution():
    def __init__(self,A,M,N):
        self.A = A
        self.B = [i for i in range(N)]
        self.l = N
        self.M = M
        self.ans = 0
        self.aux = None
    
    def solve(self,):
        arr = self.getA(0,8)
        for x in arr:
            self.aux = x
            self.dfs(0,self.M,8,0)

    def getA(self,i,s):
        if s == 0:
            return [[]]
        elif self.l-i == s:
            return [[self.B[j] for j in range(i,self.l)]]
        else:
            a = self.B[i]
            biglist = self.getA(i+1,s)
            aux = self.getA(i+1,s-1)
            for x in aux:
                biglist.append([a]+x)
            return biglist

    def dfs(self,j,M,cards,suma):
        if cards == 0:
            self.ans = max(self.ans,suma)
            return None
        i = self.aux[j]
        for y in range(self.A[i][0]):
            past = self.A[i][2][y]
            if M < past:
                return None
            self.dfs(j+1,M-past,cards-1,suma+self.A[i][1][y])

T = int(input())
for i in range(T):
    M, N = map(int,raw_input().split())
    A = []
    for x in range(N):
        lvls, lvl = map(int,raw_input().split())
        B = list(map(int,raw_input().split()))[lvl-1:lvls]
        C = list(map(int,raw_input().split()))[lvl-1:lvls]
        D = [0]
        past = 0
        for y in C:
            past += y
            D.append(past)
        A.append([lvls+1-lvl,B,D])
    sol = Solution(A,M,N)
    sol.solve()
    print('Case #{}: {}'.format(i+1,sol.ans))