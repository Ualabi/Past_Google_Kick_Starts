# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83dc

def getIndex(s):
    direc = {'E', 'W', 'S', 'N'}
    j,k = 0,0
    x = 0
    while x < len(s):
        if s[x] in direc:
            if s[x] == 'E':     j += 1
            elif s[x] == 'W':   j -= 1
            elif s[x] == 'S':   k += 1
            elif s[x] == 'N':   k -= 1
            x += 1
        elif s[x] == ')':
            x += 1
            break
        else:
            t = int(s[x])
            sj, sk, sx = getIndex(s[x+2:])
            x += sx+2
            j += t*sj
            k += t*sk
    return j,k,x
            
fx, fy = 10**9, 10**9
T = int(input())
for i in range(T):
    s = input()
    j,k,x = getIndex(s)
    j %= 10**9
    k %= 10**9
    print('Case #{}: {} {}'.format(i+1,j+1,k+1))
