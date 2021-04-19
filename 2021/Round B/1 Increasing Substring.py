# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882

T = int(input())
for t in range(T):
    N = int(input())
    word = input()
    
    ans = [1]
    l,r = 0,1
    while r < N:
        if word[r-1] < word[r]:
            ans.append(r+1-l)
            r += 1
        else:
            ans.append(1)
            l = r
            r += 1
    
    print('Case #{}: {}'.format(t+1, ' '.join(map(str,ans))))