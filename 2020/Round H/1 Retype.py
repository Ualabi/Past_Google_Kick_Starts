# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043adc7

T = int(input())
for t in range(T):
    N,K,S = map(int,input().split())
    
    t1 = K+N
    t2 = K-1+(K-S)+N-S+1
    
    print('Case #{}: {}'.format(t+1,min(t1,t2)))