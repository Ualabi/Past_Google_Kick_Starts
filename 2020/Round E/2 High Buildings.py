# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef73

T = int(input())
for t in range(T):
    N, A, B, C = map(int,input().split())
    if N < A+B-C:
        ans = 'IMPOSSIBLE'
    elif N == 1:
        ans = '1'
    elif N == 2:
        if A == 2 and B == 2 and C == 2:
            ans = '1 1'
        elif A == 1 and B == 2 and C == 1:
            ans = '2 1'
        elif A == 2 and B == 1 and C == 1:
            ans = '1 2'
        else:
            ans = 'IMPOSSIBLE'
    elif A == 1 and B == 1:
        ans = 'IMPOSSIBLE'
    elif A == B and A == C:
        ans = '2 '*(A-1) + '1 '*(N-A) + '2 '
    elif A == C:
        ans = '3 '*(A) + '1 '*(N-B) + '2 '*(B-A)
    elif B == C:
        ans = '2 '*(A-B) + '1 '*(N-A) + '3 '*(B)
    else:
        ans = '2 '*(A-C) + '3 '*C + '1 '*(N-A-B+C) + '2 '*(B-C)
    
    print('Case #{}: {}'.format(t+1,ans))