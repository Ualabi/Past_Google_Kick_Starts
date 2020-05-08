# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201dbb
# Use PyPy2 to run it, it does not pass the TLE with Python 3/2

ax = [-1,1,0,0]
ay = [0,0,-1,1]
maxim = float('inf')

T = int(input())
for i in range(T):
    ans = 0
    R, C = map(int,raw_input().split())
    arr = []
    for ii in range(R):
        arr.append(list(map(int,raw_input().split())))
    
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
                                if a == 0 or b == 0 or a == R-1 or b == C-1:
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
                
    print('Case #'+str(i+1)+': '+str(ans))