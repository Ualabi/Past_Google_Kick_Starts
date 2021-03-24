# Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b0c6

i = set('13579')
p = set('02468')
pow5 = [1]
for x in range(18):
    pow5.append(pow5[-1]*5)
pow0 = [0]
for x in range(1,19):
    pow0.append(pow0[-1]+pow5[x])

def isBoring(N):
    flag = True
    for n in str(N):
        if (flag and n in p) or (not flag and n in i):
            return 0
        flag = not flag
    return 1

def solve(N):
    ans = pow0[(len(str(N))-1)]
    
    flag = True
    SN = str(N)
    l = len(SN)-1
    for n in SN:
        # print(ans)
        if flag:
            aux = int(n)//2
            ans += aux*pow5[l]
        else:
            aux = (int(n)+1)//2
            ans += aux*pow5[l]
        if (flag and n in p) or (not flag and n in i):
            break
        l -= 1
        flag = not flag
    # print('->',ans)
    return ans + isBoring(N)

    
T = int(input())
for t in range(T):
    L,R = map(int,input().split())
    ans = solve(R) - solve(L) + isBoring(L)
    print('Case #{}: {}'.format(t+1,ans))