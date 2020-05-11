# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201ca3
# Does not pass the TLE for the second Test Set

class Solution():
    def __init__(self,A):
        self.A = A
        self.ans = 0
    
    def dfs(self,i,M,N,cards,suma):
        if cards == 0:
            self.ans = max(self.ans,suma)
            return None
            
        for y in range(self.A[i][0]):
            past = self.A[i][2][y]
            if M < past:
                break
            self.dfs(i+1,M-past,N-1,cards-1,suma+self.A[i][1][y])
            
        if N-i-1 > cards:
            self.dfs(i+1,M,N-1,cards,suma)
        return None
        

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
    sol = Solution(A)
    sol.dfs(0,M,N,8,0)
    print('Case #{}: {}'.format(i+1,sol.ans))
