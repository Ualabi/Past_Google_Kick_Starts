T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    
    freq = {}
    for a in A:
        freq[a] = freq.get(a,0) + 1
    
    val = sorted(freq)
    lim = len(val)
        
    past = 0    
    suma = {}
    for f in val:
        past += freq[f]
        suma[f] = past
        
    ans = 0
    for a in range(lim):
        f = freq[val[a]]
        if 3 <= f:
            for b in range(a,lim):
                if 3*val[a] <= val[b]:
                    break
            if a < b:
                x = suma[b] - f
            elif b == a and a > 0:
                x = suma[val[a-1]]
            else:
                x = 0
            p = (f*(f-1)*(f-2))//6
            ans += x*p
        
        if 2 <= f:
            x = 0
            for b in range(lim):
                if b != a:
                    y = freq[val[b]]
                    z = 0 
                    for c in range(b+1,lim):
                        if c != a:
                            if val[c] < val[b] + 2*val[a]:
                                z += freq[val[c]]
                            else:
                                break
                    x += y*z
            p = (f*(f-1))//2
            ans += x*p
        
        
        # if 2 <= f:
        #     x = 0
        #     for b in range(lim-1):
        #         if b != a:
        #             print(val[a],val[b])
        #             y = freq[val[b]]
        #             z = 0 
        #             for c in range(b+1,lim):
        #                 if c != a:
        #                     if val[b] + 2*val[a] <= val[c]:
        #                         break
                    
        #             if val[c] < val[b] + 2*val[a]:
        #                 if a == c:
        #                     if a-1 == b:
        #                         z = 0
        #                     else:
        #                         z = suma[val[a-1]] - suma[val[b]]
        #                 elif a < c and a < b:
        #                     z = suma[val[c]] - suma[val[b]]
        #                 elif a < c:
        #                     z = suma[val[c]] - f - suma[val[b]] 
        #                 else:
        #                     z = suma[val[c]] - suma[val[b]]
        #             else:
        #                 z = 0
        #             print('-',y,z)
        #             x += y*z
        #     p = (f*(f-1))//2
        #     ans += x*p

            # x = 0
            # for b in range(lim-1):
            #     if b != a:
            #         y = freq[val[b]]
            #         l, r = b+1, lim-1
            #         while l < r:
            #             if l+1 == r:
            #                 k = r
            #             else:
            #                 k = (l+r)//2
                            
            #             if val[k] < val[b] + 2*val[a]:
            #                 l = k
            #             else:
            #                 r = k-1
                    
            #         if val[l] < val[b] + 2*val[a]:
            #             if a == l:
            #                 if a-1 == b:
            #                     z = 0
            #                 else:
            #                     z = suma[val[a-1]] - suma[val[b]]
            #             elif a < l and a < b:
            #                 z = suma[val[l]] - suma[val[b]]
            #             elif a < l:
            #                 z = suma[val[l]] - f - suma[val[b]] 
            #             else:
            #                 z = suma[val[l]] - suma[val[b]]
            #         else:
            #             z = 0

            #         x += y*z

            # p = (f*(f-1))//2
            # ans += x*p

    print('Case #{}: {}'.format(t+1,ans))