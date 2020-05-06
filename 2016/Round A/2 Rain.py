# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201dbb
def border(x,y,R,C):
    if x == 0 or y == 0 or x == R-1 or y == C-1:
        return True
    else:
        return False

def inrange(x,y,R,C):
    if x == -1 or y == -1 or x == R or y == C:
        return False
    else:
        return True

T = int(input())
for i in range(T):
    ans = 0
    R, C = map(int,input().split())
    arr = []
    for ii in range(R):
        arr.append(list(map(int,input().split())))
    
    if R <= 2 or C <= 2:
        print('Case #{}: {}'.format(i+1,0))
        continue
    
    ax = [-1,1,0,0]
    ay = [0,0,-1,1]
    checked = set()
    for x in range(1,R-1):
        for y in range(1,C-1):
            if (x,y) in checked:
                continue
            
            checked.add((x,y))
            flag = True
            limit = arr[x][y]
            queue = [(x,y)]
            lake = set()
            lake.add((x,y))
            fronter = float('inf')
            while queue:
                aux = []
                for (j,k) in queue:
                    for r in range(4):
                        a = j+ax[r]
                        b = k+ay[r]
                        if inrange(a,b,R,C):
                            if (a,b) not in lake and arr[a][b] <= limit:
                                if border(a,b,R,C):
                                    flag = False
                                if arr[a][b] == limit:
                                    checked.add((a,b))
                                lake.add((a,b))
                                aux.append((a,b))
                            elif arr[a][b] > limit:
                                fronter = min(fronter,arr[a][b])
                queue = aux
                
            if flag:
                for (j,k) in lake:
                    ans += fronter - arr[j][k]
                    arr[j][k] = fronter
            
    print('Case #{}: {}'.format(i+1,ans))