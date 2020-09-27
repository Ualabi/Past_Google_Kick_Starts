import copy

def minmax(S, board, ra, ca, rb, cb, turno, suma, poss):
    if poss == 3:
        return suma
    
    # print(board,suma,turno)
    if turno:
        turno = not turno
        suma += 1
        flag = False
        a, b, c, d = -100, -100, -100, -100
        
        if 0 < ca and board[ra][ca-1]:
            flag = True
            nboard = copy.deepcopy(board)
            nboard[ra][ca-1] = False
            a = minmax(S, nboard, ra, ca-1, rb, cb, turno, suma, poss)
                
        if ca < 2*ra and board[ra][ca+1]:
            flag = True
            nboard = copy.deepcopy(board)
            nboard[ra][ca+1] = False
            b = minmax(S, nboard, ra, ca+1, rb, cb, turno, suma, poss)
            
        if ca%2==0 and ra < S-1 and board[ra+1][ca+1]:
            flag = True
            nboard = copy.deepcopy(board)
            nboard[ra+1][ca+1] = False
            c = minmax(S, nboard, ra+1, ca+1, rb, cb, turno, suma, poss)

        if ca%2 == 1 and board[ra-1][ca-1]:
            flag = True
            nboard = copy.deepcopy(board)
            nboard[ra-1][ca-1] = False
            d = minmax(S, nboard, ra-1, ca-1, rb, cb, turno, suma, poss)
            
        if flag:
            return max(a,b,c,d)
        else:
            return minmax(S, board, ra, ca, rb, cb, turno, suma-1, poss|1)

    else:
        turno = not turno
        suma -= 1
        flag = False
        a, b, c, d = 100, 100, 100, 100
        
        if 0 < cb and board[rb][cb-1]:
            flag = True
            nboard = copy.deepcopy(board)
            nboard[rb][cb-1] = False
            a = minmax(S, nboard, ra, ca, rb, cb-1, turno, suma, poss)
                
        if cb < 2*rb and board[rb][cb+1]:
            flag = True
            nboard = copy.deepcopy(board)
            nboard[rb][cb+1] = False
            b = minmax(S, nboard, ra, ca, rb, cb+1, turno, suma, poss)
            
        if cb%2==0 and rb < S-1 and board[rb+1][cb+1]:
            flag = True
            nboard = copy.deepcopy(board)
            nboard[rb+1][cb+1] = False
            c = minmax(S, nboard, ra, ca, rb+1, cb+1, turno, suma, poss)

        if cb%2 == 1 and board[rb-1][cb-1]:
            flag = True
            nboard = copy.deepcopy(board)
            nboard[rb-1][cb-1] = False
            d = minmax(S, nboard, ra, ca, rb-1, cb-1, turno, suma, poss)
            
        if flag:
            return min(a,b,c,d)
        else:
            return minmax(S, board, ra, ca, rb, cb, turno, suma+1, poss|2)

T = int(input())
for t in range(T):
    S, RA, PA, RB, PB, C = map(int,input().split())
    board = [[True for _ in range(2*S)] for __ in range(S)]
    board[RA-1][PA-1] = False
    board[RB-1][PB-1] = False
    for c in range(C):
        a,b = map(int,input().split())
        board[a-1][b-1] = False
    ans = minmax(S,board,RA-1,PA-1,RB-1,PB-1,True, 0, 0)
    print('Case #{}: {}'.format(t+1,ans))

"""
1
2 1 1 2 1 0
2 2 2 1 1 2
2 1
2 3
"""