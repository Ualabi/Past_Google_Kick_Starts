# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3

T = int(input())
for t in range(T):
    N, K = map(int,input().split())
    word = input()
    
    curr = N//2
    for i in range(N//2):
        if word[i] == word[N-i-1]:
            curr -= 1
    
    ans = abs(K-curr)
    print('Case #{}: {}'.format(t+1,ans))