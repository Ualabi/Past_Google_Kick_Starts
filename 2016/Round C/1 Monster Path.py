# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c0a/0000000000201ca4

from copy import deepcopy as dc

def dfs(m,suma,mapa,R,C,Rs,Cs,p,q,S,s):
    if 0 <= Rs and Rs < R and 0 <= Cs and Cs < C:
        if mapa[Rs][Cs][1] > S:
            return m
        val = p[mapa[Rs][Cs][1]] if mapa[Rs][Cs][0] else q[mapa[Rs][Cs][1]]
        mapa[Rs][Cs][1] += 1
        suma += val
        if s == S:
            return max(m,suma)
        else:
            if m >= suma + (S-s)*p[0]:
                return m
            else:
                u = dfs(m,suma,dc(mapa),R,C,Rs-1,Cs,p,q,S,s+1)
                d = dfs(u,suma,dc(mapa),R,C,Rs+1,Cs,p,q,S,s+1)
                l = dfs(d,suma,dc(mapa),R,C,Rs,Cs-1,p,q,S,s+1)
                r = dfs(l,suma,dc(mapa),R,C,Rs,Cs+1,p,q,S,s+1)
                return r
    else:
        return m

T = int(input())
for t in range(T):
    R, C, Rs, Cs, S = map(int,input().split())
    P, Q = map(float,input().split())
    
    mapa = []
    for x in range(R):
        aux = input().split()
        m = []
        for y in aux:
            if y == 'A':
                m.append([True,0])
            else:
                m.append([False,0])
        mapa.append(m)
    
    pp, qq = 0, 0
    p, q = [], []
    for x in range(S+1):
        p.append((1-pp)*P)
        q.append((1-qq)*Q)
        pp += p[-1]
        qq += q[-1]

    u = dfs(0,0,dc(mapa),R,C,Rs-1,Cs,p,q,S,1)
    d = dfs(u,0,dc(mapa),R,C,Rs+1,Cs,p,q,S,1)
    l = dfs(d,0,dc(mapa),R,C,Rs,Cs-1,p,q,S,1)
    r = dfs(l,0,dc(mapa),R,C,Rs,Cs+1,p,q,S,1)

    print('Case #{}: {}'.format(t+1,r))