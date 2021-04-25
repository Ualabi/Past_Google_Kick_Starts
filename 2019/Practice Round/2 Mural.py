# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/0000000000058b89

T = int(input())
for t in range(T):
    N = int(input())
    A = input()
    arr = []
    for a in str(A):
        arr.append(int(a))
    
    ans = 0
    cl = N//2 + N%2
    count, l, c = 0, 0, 0
    for x in arr:
        if c == cl:
            count += x
            count -= arr[l]
            l += 1
        else:
            count += x
            c += 1
        ans = max(count, ans)
    
    print('Case #{}: {}'.format(t+1,ans))