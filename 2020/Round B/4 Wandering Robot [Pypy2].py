# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565
# Use PyPy2 to run it, it does not pass the TLE with Python 3/2

from math import log
logs = [0]
for x in range(1,2*10**5):
    logs.append(logs[x-1] + log(x,2))

T = int(input())
for i in range(T):
    W, H, L, U, R, D = map(int,raw_input().split())
    
    if (L == 1 and U == 1) or (D-U+1 == H) or (R-L+1 == W):
        print('Case #'+str(i+1)+': 0.0')
        continue
    
    count = 0
    if 1 < L and D < H:
        d, w = D, L-2
        while w >= 0:
            count += 2**(logs[d+w] - logs[d] - logs[w] - d - w)
            d += 1
            w -= 1
            
    if 1 < U and R < W:
        r, h = R, U-2
        while h >= 0:
            count += 2**(logs[r+h] - logs[r] - logs[h] - r - h)
            r += 1
            h -= 1
    
    print('Case #'+str(i+1)+': '+str(count))