# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003379bb

def dfs(letras,taken,word):
    if len(letras) == len(taken):
        return word
    for x in letras:
        if x not in taken:
            if len(letras[x] - taken) == 0:
                w = dfs(letras,taken | {x},word+x)
                if w != -1:
                    return w
    return -1

def solve(arr,R,C):
    letras = {}
    for r in range(R):
        for c in range(C):
            if r == R-1:
                if arr[r][c] not in letras:
                    letras[arr[r][c]] = set()
            else:
                if arr[r][c] not in letras:
                    letras[arr[r][c]] = set() 
                if arr[r+1][c] != arr[r][c]:
                    letras[arr[r][c]].add(arr[r+1][c])
    return dfs(letras,set(),'')

T = int(input())
for t in range(T):
    R, C = map(int,input().split())
    arr = []
    for x in range(R):
        aux = list(input())
        arr.append(aux)
    print('Case #{}: {}'.format(t+1,solve(arr,R,C)))