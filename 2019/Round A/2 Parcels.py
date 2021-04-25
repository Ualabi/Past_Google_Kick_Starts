# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/000000000006987d

def solve(arr,R,C):
    queue = []
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 1:
                queue.append((r,c))
    
    if len(queue) >= R*C-1:
        return 0
    
    v = 0
    values =  {}
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    taken = set(queue)
    while queue:
        aux = []
        values[v] = []
        for (r,c) in queue:
            values[v].append([r,c])
            for i in range(4):
                nr = r+dx[i]
                nc = c+dy[i]
                if 0<=nr and nr<R and 0<=nc and nc<C and (nr,nc) not in taken:
                    aux.append([nr,nc])
                    taken.add((nr,nc))
        queue = aux
        v += 1
    l, r = 1, v-1
    
    while l<r:
        m = (l+r)//2
        a,b,c,d = float('-inf'), float('inf'), float('-inf'), float('inf')
        for i in range(m+1,v):
            for [x,y] in values[i]:
                a = max(a,x+y)
                b = min(b,x+y)
                c = max(c,x-y)
                d = min(d,x-y)
        aux = False
        for i in range(1,v):
            for [x,y] in values[i]:
                mx = max(a-(x+y),(x+y)-b,c-(x-y),(x-y)-d)
                if mx <= m:
                    aux = True
                    break
            if aux:
                break
        if aux:
            r = m
        else:
            l = m+1
        
    return r

T = int(input())
for t in range(T):
    [R,C] = list(map(int,input().split()))
    arr = []
    for y in range(R):
        myline = input()
        aux = []
        for z in myline:
            aux.append(int(z))
        arr.append(aux)
    print('Case #{}: {}'.format(t+1,solve(arr,R,C)))
