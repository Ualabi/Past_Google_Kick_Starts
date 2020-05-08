# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3ff3

import sys 
sys.setrecursionlimit(10**6) 

class trie:
    def __init__(self):
        self.val = '*'
        self.sons = {}
    
    def add(self,word):
        curr = self.sons
        for x in word:
            curr[x] = curr.get(x,[0,{}])
            curr[x][0] += 1 
            curr = curr[x][1]
        curr['*'] = 1

def getSol(K,words):
    count = 0
    for x in words:
        if x == '*':
            continue
        [a,b] = words[x]
        if a >= K:
            count += a//K
            count += getSol(K,b)
    return count

T = int(input())
for x in range(T):
    [N,K] = list(map(int,input().split()))
    w = trie()
    for y in range(N):
        w.add(input())
    print('Case #{}: {}'.format(x+1,getSol(K,w.sons)))
