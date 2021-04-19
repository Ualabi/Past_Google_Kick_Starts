import time
start = time.time()

N = 7
primes = [2,3]
for i in range(7,10**N):
    flag = True
    for prime in primes:
        if i%prime == 0:
            flag = False
            break
        elif prime*prime > i:
            break
    if flag:
        primes.append(i)

end = time.time()
print(N, len(primes), end - start)