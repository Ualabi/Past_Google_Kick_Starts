# Link: https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414bfb

T = int(input())
for t in range(T):
    S = list(input())
    lim = len(S)
    kick = []
    start = []
    for i in range(0,lim-4):
        if S[i:i+4] == ['K','I','C','K']:
            kick.append(i)
        elif S[i:i+5] == ['S','T','A','R','T']:
            start.append(i)
    if lim >= 4:
        if S[lim-4:] == ['K','I','C','K']:
            kick.append(lim-4)
    
    def bisearch(i,N):
        l, r = 0, N-1
        while l <= r:
            m = (l+r)//2
            if i <= start[m]:
                r = m-1
            else:
                l = m+1
        return N-l
    
    ls = len(start)
    ans = 0
    for k in kick:
        ans += bisearch(k,ls)
    
    print('Case #{}: {}'.format(t+1,ans))