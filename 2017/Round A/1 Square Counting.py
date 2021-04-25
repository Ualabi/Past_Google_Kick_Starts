# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c97/0000000000201d25

m = 1000000007
T = int(input())
for t in range(T):
    R, C = map(int,input().split())
    R, C = min(R,C), max(R,C)
    ans = 0
    
    sum1toR = (R-1)*R//2
    sum1toR2= (R-1)*R*(2*R-1)//6
    sum1toR3= sum1toR*sum1toR
    
    ans = (R*C)*sum1toR
    ans -= (R+C)*sum1toR2
    ans += sum1toR3
    
    print('Case #{}: {}'.format(t+1,ans%m))