p  = {'0','2','4','6','8'}
pl = {'0':2,'2':4,'4':6,'6':8,'8':10} #to  8
pr = {'0':10,'2':8,'4':6,'6':4,'8':2} #to 10
i  = {'1','3','5','7','9'}
il = {'1':3,'3':5,'5':7,'7':9,'9':11} #to  8
ir = {'1':9,'3':7,'5':5,'7':3,'9':1 } #to 10

T = int(input())
for t in range(T):
    N = input()
    l = 10**(len(N))
    ansl = 0
    ansr = 0
    flag = False
    for x in N:
        l = l//10
        if x in p:
            if flag:
                ansl += pl[x]*l
                ansr += pr[x]*l
                flag = False
            else:
                continue
        else:
            if flag:
                ansl += il[x]*l
                ansr += ir[x]*l
                flag = False
            else:
                flag = True
                continue
    if flag:
        ansl += 1
        ansr += 1
    print('Case #{}: {}'.format(t+1,min(ansl,ansr)))