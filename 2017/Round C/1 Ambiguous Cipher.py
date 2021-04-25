# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c98/0000000000201d26

T = int(input())
for t in range(T):
    W = input()
    ln = len(W)
    if ln%2 == 1:
        print('Case #{}: AMBIGUOUS'.format(t+1))
        continue

    ans = ['']*ln
    ans[1], ans[-2] = W[0], W[-1]
    for x in range(0,ln+1):
        if x%2 == 1 and 1 < x:
            ans[x] = chr((26 + (ord(W[x-1])-65) - (ord(ans[x-2])-65))%26 + 65)
        elif x%2 == 0 and 2 < x:
            y = ln-x
            ans[y] = chr((26 + (ord(W[y+1])-65) - (ord(ans[y+2])-65))%26 + 65)
            
    print('Case #{}: {}'.format(t+1,''.join(ans)))