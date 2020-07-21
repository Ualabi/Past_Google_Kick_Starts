class Solution:
    def exist(self, board, word):
        R = len(board)
        C = len(board[0])
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        starts = []
        for r in range(R):
            for c in range(C):
                key = board[r][c]
                if key == word[0]:
                    starts.append((r,c))
        
        mapa = [[{} for c in range(C)] for r in range(R)]
        for r in range(R):
            for c in range(C):
                key = board[r][c]
                for d in range(4):
                    nr = r+dx[d]
                    nc = c+dy[d]
                    if 0<=nr and nr<R and 0<=nc and nc<C:
                        nkey = board[nr][nc]
                        mapa[r][c][nkey] = mapa[r][c].get(nkey,[]) + [(nr,nc)]
            
        def dfs(w,r,c,visited):
            print(w,r,c)
            if len(w) == 0:
                return True
            
            key = w[0]
            nw = w[1:]
            
            if key in mapa[r][c]:
                for (nr,nc) in mapa[r][c][key]:
                    if (nr,nc) not in visited:
                        if dfs(nw,nr,nc,visited^{(nr,nc)}):
                            return True
            return False
        
        print(starts)
        for x in range(R):
            for y in range(C):
                print(x,y,mapa[x][y])

        nword = word[1:]
        for (r,c) in starts:
            if dfs(nword,r,c,{(r,c)}):
                return True
        
        return False

sol = Solution()
A = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
B = "SEE"

aux = sol.exist(A,B)
print(aux)