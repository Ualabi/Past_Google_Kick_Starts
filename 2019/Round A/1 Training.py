# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/00000000000698d6

def getBestGroup(nums,P,maxi=float('inf')):
    for x in range(P,len(nums)+1):
        if x == P:
            suma = sum(nums[:P])
        else:
            suma += - nums[x-P-1] + nums[x-1] 

        top = nums[x-P]*P
        dif = top - suma

        if dif < maxi and 0 <= dif:
            maxi = dif
    return maxi
    
T = int(input())

for x in range(T):
    [N, P] = list(map(int,input().split()))
    nums = sorted(list(map(int,input().split())),reverse=True)
    print('Case #{}: {}'.format(x+1,getBestGroup(nums,P)))