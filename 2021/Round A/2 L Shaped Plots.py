# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509

memo = [[0 for _ in range(1001)] for _ in range(1001)]
for r in range(2,1001):
    for c in range(2,1001):
        memo[r][c] = min(r//2,c)+min(r,c//2)-2

T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    
    board = []
    for r in range(R):
        aux = list(map(int, input().split()))
        board.append(aux)
        
    dataN = [[0 for _ in range(C)] for _ in range(R)]
    dataS = [[0 for _ in range(C)] for _ in range(R)]
    dataW = [[0 for _ in range(C)] for _ in range(R)]
    dataE = [[0 for _ in range(C)] for _ in range(R)]
    
    for r in range(R):
        cntW, cntE = 0, 0
        for c in range(C):
            cntW = cntW+1 if board[r][c]==1 else 0
            cntE = cntE+1 if board[r][C-c-1]==1 else 0
            dataW[r][c] = cntW
            dataE[r][C-c-1] = cntE
    
    for c in range(C):
        cntN, cntS = 0, 0
        for r in range(R):
            cntN = cntN+1 if board[r][c]==1 else 0
            cntS = cntS+1 if board[R-r-1][c]==1 else 0
            dataN[r][c] = cntN
            dataS[R-r-1][c] = cntS
            
    ans = 0
    for r in range(R):
        for c in range(C):
            ans += memo[dataW[r][c]][dataN[r][c]]
            ans += memo[dataE[r][c]][dataN[r][c]]
            ans += memo[dataW[r][c]][dataS[r][c]]
            ans += memo[dataE[r][c]][dataS[r][c]]
            
    print('Case #{}: {}'.format(t+1,ans))