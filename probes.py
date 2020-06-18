def solve(F):
    end = F
    F = F-F%10
    start = F
    ans = 0
    m = 1
    while F:
        y = F%10
        ans += y*m
        m *= 9
        F = F//10
        
    ans = 8 * ans//9
    for i in range(start,end+1):
        if "9" not in str(i) and i%9!=0:
            ans += 1
    return ans

T = int(input())
for t in range(T):
    F, L = map(int,input().split())
    a = solve(L)
    b = solve(F)
    ans = a - b + 1
    print('Case #{}: {}'.format(t+1,ans))