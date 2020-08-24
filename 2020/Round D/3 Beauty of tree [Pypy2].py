# Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd

T = int(input())
for t in range(T):
    N, A, B = map(int,raw_input().split())
    arr = list(map(int,raw_input().split()))
    A = [A,B]
    par = [[0 for _ in range(20)] for __ in range(N)]
    depth = [0 for _ in range(N)]
    for i in range(1,N):
        par[i][0] = arr[i-1]-1
        depth[i] = depth[par[i][0]]+1
        z = 0
        while 0 < par[i][z]:
            par[i][z+1] = par[par[i][z]][z]
            z += 1
    ans = 0
    cnt = [[0 for _ in range(2)] for __ in range(N)]
    for i in range(N-1,-1,-1):
        for z in range(2):
            cnt[i][z] += 1
            if (depth[i] < A[z]):
                continue
            cur = i
            l, v = 0, A[z]
            while 0 < v:
                if 0 < (v & 1):
                    cur = par[cur][l]
                v >>= 1
                l += 1
            cnt[cur][z] += cnt[i][z]
        va = (cnt[i][0]+0.0) / N
        vb = (cnt[i][1]+0.0) / N
        ans += va + vb - va*vb
    print('Case #{}: {}'.format(t+1,ans))