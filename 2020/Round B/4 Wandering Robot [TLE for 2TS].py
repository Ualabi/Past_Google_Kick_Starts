# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565
# This algoritgm didnt pass the TLE for the second test set in python 3, but it did in c++, thats why I attached both solutions

from numpy import log2 as log2
logs = [0]
for x in range(1,2*10**5):
    logs.append(logs[x-1] + log2(x))

T = int(input())
for i in range(T):
    W, H, L, U, R, D = map(int,input().split())
    
    if (L == 1 and U == 1) or (D-U+1 == H) or (R-L+1 == W):
        print('Case #{}: 0.0'.format(i+1))
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

    print('Case #{}: {}'.format(i+1,count))
