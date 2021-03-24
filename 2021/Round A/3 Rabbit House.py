# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14

T = int(input())
for t in range(T):
    R,C = map(int,input().split())
    
    maxim = 0
    board = []
    for r in range(R):
        aux = list(map(int,input().split()))
        maxim = max(maxim, max(aux))
        board.append(aux)
    
    freq = {}
    for r in range(R):
        for c in range(C):
            val = board[r][c]
            if val not in freq:
                freq[val] = set()
            freq[val].add((r,c))
            
    ans = 0
    curr = maxim
    checked = freq[curr]
    queue = list(checked)
    vals = [(0,-1),(0,1),(1,0),(-1,0)]
    
    while queue and 2<=curr:
        nqueue = []
        curr -= 1
        for (r,c) in queue:
            for (i,j) in vals:
                nr = r+i
                nc = c+j
                if 0<=nr and nr<R and 0<=nc and nc<C:
                    cell = (nr,nc)
                    if cell not in checked:
                        checked.add(cell)
                        nqueue.append(cell)
                        ans += (curr - board[nr][nc])
                        freq[board[nr][nc]].remove((nr,nc))
                        
        queue = nqueue
        if curr in freq:
            for (r,c) in freq[curr]:
                queue.append([r,c])
                checked.add((r,c))
            
    print('Case #{}: {}'.format(t+1,ans))