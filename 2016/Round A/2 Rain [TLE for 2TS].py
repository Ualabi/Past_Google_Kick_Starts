# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201dbb

ax = [-1,1,0,0]
ay = [0,0,-1,1]
maxim = float('inf')

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
    
    checked = set()
    for x in range(1,R-1):
        for y in range(1,C-1):
            if (x,y) not in checked:
                checked.add((x,y))
                flag = True
                limit = arr[x][y]
                queue = [(x,y)]
                lake = set()
                lake.add((x,y))
                fronter = maxim
                while queue:
                    aux = []
                    for (j,k) in queue:
                        for r in range(4):
                            a = j+ax[r]
                            b = k+ay[r]
                            if (a,b) not in lake and arr[a][b] <= limit:
                                if x == 0 or y == 0 or x == R-1 or y == C-1:
                                    flag = False
                                else:
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

# 1
# 10 10
# 5 4 6 5 2 3 1 2 2 6
# 7 5 3 1 5 1 3 7 6 2
# 1 1 5 6 1 1 1 2 1 7
# 2 2 2 3 7 6 1 2 6 4
# 6 1 7 3 4 2 3 6 4 5
# 6 2 2 6 7 6 1 7 7 2
# 4 1 3 2 1 7 5 7 2 6
# 5 3 2 6 1 1 1 7 2 2
# 1 7 2 5 4 3 1 7 3 1
# 2 2 3 6 7 7 3 5 2 6
