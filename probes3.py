ans = []
for i in range(q):
    x, y = 0, 0
    # scanf("%d%d", &x, &y);
    if (y == 1):
        ans.append(x)
        continue
    x += n
    for j in range(19,-1,-1):
        if (f[x][j] > 0 and sz[f[x][j]] < y):
            x = f[x][j]
    if (l[f[x][0]] == x):
        ans.append(f[x][0] + y - sz[x]) 
    else:
        ans.append(f[x][0] - y + sz[x] + 1)

        