# Link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150aac

T = int(input())
for t in range(T):
    N, R, C, Sr, Sc = map(int,input().split())
    dirs = input()
    inter={ 'N':{(Sr,Sc):(Sr-1)},
            'S':{(Sr,Sc):(Sr+1)},
            'E':{(Sr,Sc):(Sc+1)},
            'W':{(Sr,Sc):(Sc-1)}}
    for d in dirs:
        if d in 'NS':
            p = 'S' if d == 'N' else 'N'
            s = 1 if d == 'S' else -1
            Sr = inter[d][(Sr,Sc)]
            inter[p][(Sr,Sc)] = inter[p].get((Sr-s,Sc),Sr-s) 
            inter[d][(Sr,Sc)] = inter[d].get((Sr+s,Sc),Sr+s) 
            inter['E'][(Sr,Sc)] = inter['E'].get((Sr,Sc+1),Sc+1) 
            inter['W'][(Sr,Sc)] = inter['W'].get((Sr,Sc-1),Sc-1) 
        elif d in 'EW':
            p = 'W' if d == 'E' else 'E'
            s = 1 if d == 'E' else -1
            Sc = inter[d][(Sr,Sc)]
            inter[p][(Sr,Sc)] = inter[p].get((Sr,Sc-s),Sc-s) 
            inter[d][(Sr,Sc)] = inter[d].get((Sr,Sc+s),Sc+s) 
            inter['N'][(Sr,Sc)] = inter['N'].get((Sr-1,Sc),Sr-1) 
            inter['S'][(Sr,Sc)] = inter['S'].get((Sr+1,Sc),Sr+1) 
        Srn = inter['N'][(Sr,Sc)]+1
        Srs = inter['S'][(Sr,Sc)]-1
        Sce = inter['E'][(Sr,Sc)]-1
        Scw = inter['W'][(Sr,Sc)]+1
        inter['N'][(Srs,Sc)] = Srn - 1
        inter['S'][(Srn,Sc)] = Srs + 1
        inter['E'][(Sr,Scw)] = Sce + 1
        inter['W'][(Sr,Sce)] = Scw - 1
    print('Case #{}: {} {}'.format(t+1,Sr,Sc))