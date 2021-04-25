# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a8e6

primes = []
for i in range(2,10**5):
    flag = True
    for prime in primes:
        if i%prime == 0:
            flag = False
            break
        elif prime*prime > i:
            break
    if flag:
        primes.append(i)
        
def check(num):
    flag = False
    for prime in primes:
        if num == prime:
            break
        elif num%prime == 0:
            flag = True
            break
        elif num < prime*prime:
            break
    return flag

T = int(input())
for t in range(T):
    N = int(input())
    M = int(N**0.5)
    
    m, r = M, M+1
    while check(m):
        m -= 1
    while check(r):
        r += 1
    
    if m*r <= N:
        print('Case #{}: {}'.format(t+1, m*r))
        continue
    
    l = m-2
    while check(l):
        l -= 1
    print('Case #{}: {}'.format(t+1, l*m))
    