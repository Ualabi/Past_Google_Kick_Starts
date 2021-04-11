# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/00000000000510ed

i = {'1':'0','3':'2','5':'4','7':'6','9':'8'}
p = {'0':'2','1':'2','2':'4','3':'4','4':'6','5':'6','6':'8','7':'8','8':'0','9':'0'}

T = int(input())
for t in range(T):
    sN = input()
    N = int(sN)
    l, r = '', []
    fl, fr = True, True
    for x in sN:
        if x in i:
            if fl:
                l += i[x]
                fl = False
            else:
                l += '8'
            
            if fr:
                if x == '9':
                    ff = True
                    for y in r:
                        if y != '8':
                            ff = False
                            break
                    if ff:
                        r = ['2','0']+['0']*len(r)
                    else:
                        y = len(r)-1
                        while r[y] == '8':
                            r[y] = '0'
                            y -= 1
                        r[y] = p[r[y]]
                        r += ['0']
                else:
                    r += [p[x]]
                        
                fr = False
            else:
                r += '0'
        else:
            l += x if fl else '8'
            r += [x] if fr else ['0']

    r = ''.join(r)
    if sN == l or sN == r:
        print('Case #{}: {}'.format(t+1,0))
    else:
        print('Case #{}: {}'.format(t+1,min(N-int(l),int(r)-N)))