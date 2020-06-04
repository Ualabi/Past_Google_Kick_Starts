# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca0/0000000000201d2f

T = int(input())
for t in range(T):
    S = input()
    I, J = map(int,input().split())
    I, J = I-1, J-1
    l = len(S)
    i, j = I%l, J%l
    if I//l == J//l:
        ans = 0
        for s in range(l):
            if S[s] == 'B':
                if i <= s and s <= j:
                    ans += 1
        print('Case #{}: {}'.format(t+1,ans))
    else:
        a, b, c = 0, 0, 0
        for s in range(l):
            if S[s] == 'B':
                a += 1
                if i <= s:
                    b += 1
                if s <= j:
                    c += 1
        i = I+l-I%l
        j = J-J%l
        k = (j-i)//l
        ans = a*k + b + c
        print('Case #{}: {}'.format(t+1,ans))