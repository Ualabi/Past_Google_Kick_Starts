# Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/0000000000337b4d
# Use PyPy2 to run it, it does not pass the TLE with Python 3/2

class SegmentTree():
    def build(self,arr,N):
        deep, lvl = 1, 1
        while lvl < N:
            deep += 1
            lvl *= 2
        self.N = N
        self.deep = deep
        self.values = [[None]]

        lvl = 2*self.N
        for x in range(self.deep):
            s = []
            sub, index = 1, 0
            lvl = lvl//2+1 if lvl%2 else lvl//2
            for y in range(lvl):
                suma = 0
                if x:
                    while index < len(self.values[x]) and index < 2*sub:
                        suma += self.values[x][index]
                        index += 1
                else:
                    suma += arr[index]
                    index += 1
                s.append(suma)
                sub += 1
            self.values.append(s)
        return None
    
    def update(self,index,nval):
        pval = self.values[1][index]
        change = nval-pval
        for x in range(self.deep):
            self.values[x+1][index] += change
            index = index//2
        return None
    
    def query(self,l,r,lvl=None):
        if lvl == None:
            lvl = self.deep
        if l==r or lvl == 0:
            return 0
        a = l//(2**(lvl-1))+1 if l%(2**(lvl-1)) else l//(2**(lvl-1))
        b = r//(2**(lvl-1))  
        if a < b:
            if   a+1 == b:
                suma = self.values[lvl][a]
            elif a+2 == b:
                suma = self.values[lvl][a] + self.values[lvl][a+1] 
            ll = a*(2**(lvl-1))
            rr = b*(2**(lvl-1))
            return self.query(l,ll,lvl-1) + suma + self.query(rr,r,lvl-1)
        else:
            return self.query(l,r,lvl-1)

T = int(input())
for t in range(T):
    N, Q = map(int,raw_input().split())
    A = list(map(int,raw_input().split()))
    
    at = [0]
    for n in range(1,N+1):
        s = 1 if n%2 else -1
        at.append(s*A[n-1])
    sat = SegmentTree()
    sat.build(at,N+1)
    
    am = [0]
    for n in range(1,N+1):
        s = 1 if n%2 else -1
        am.append(s*A[n-1]*n)
    sam = SegmentTree()
    sam.build(am,N+1)
    
    ans = 0
    for q in range(Q):
        a, b, c = raw_input().split()
        if a == 'Q':
            l, r = int(b), int(c)
            s = 1 if l%2 else -1
            ans += s*(sam.query(l,r+1)-(l-1)*sat.query(l,r+1))
        else: #a == 'U'
            i, v = int(b), int(c)
            s = 1 if i%2 else -1
            sat.update(i,s*v)
            sam.update(i,s*v*i)
    print('Case #{}: {}'.format(t+1,ans))