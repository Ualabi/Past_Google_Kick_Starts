# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/0000000000119866

T = int(input())
for t in range(T):
    N, Q = map(int,input().split())
    word = input()
    
    freq = [0 for _ in range(26)]
    frqs = [freq[:]]
    for w in word:
        freq[ord(w)-65] += 1
        frqs.append(freq[:])
    
    ans = 0
    for q in range(Q):
        l, r = map(int,input().split())
        fl, fr = frqs[l-1], frqs[r]
        
        i = 0
        for n in range(26):
            if (fr[n]-fl[n])%2 == 1:
                i += 1
        
        if (r-l)%2 == 0 and i == 1:
            ans += 1
        elif (r-l)%2 == 1 and i == 0:
            ans += 1
    
    print('Case #{}: {}'.format(t+1,ans))