# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee0/0000000000051005

import sys 
sys.setrecursionlimit(10**6) 

def getCicle(frm,act):
    global mapa, past, inde, flag, cicle
    for x in mapa[act]:
        if flag:
            break
        elif x != frm:
            if x in past:
                i = inde.index(x)
                cicle = set(inde[i:])
                flag = True
                break
            else:
                past.add(x)
                inde.append(x)
                getCicle(act,x)
    if not flag and inde[-1] == act:
        inde.pop()
        past.remove(act)

def getAns():
    global mapa, cicle, N
    queue = []
    outlist = [-1] * N
    for x in cicle:
        for y in mapa[x]:
            if y not in cicle:
                queue.append(y)
        outlist[x-1] = 0
    lvl = 1
    while queue:
        aux = []
        for ele in queue:
            outlist[ele-1] = lvl
            cicle.add(ele)
            for x in mapa[ele]:
                if x not in cicle:
                    aux.append(x)
        queue = aux
        lvl += 1
    ans = ''
    for x in outlist:
        ans += str(x) + ' '
    return ans[:-1]

T = int(input())
for t in range(T):
    N = int(input())
    mapa = {}
    for n in range(N):
        a, b = map(int,input().split())
        if a not in mapa:
            mapa[a] = []
        if b not in mapa:
            mapa[b] = []
        mapa[a].append(b)
        mapa[b].append(a)
    
    past = {1}
    inde = [1]
    flag = False
    cicle = set()
    getCicle(-1,1)
    ans = getAns()
    print('Case #{}: {}'.format(t+1,ans))