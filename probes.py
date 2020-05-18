T = int(input())
for t in range(T):
    N, R, C, Sr, Sc = map(int,input().split())
    dirs = input()
    
    inter={ 'N':{(Sr,Sc):(Sr-1)},
            'S':{(Sr,Sc):(Sr+1)},
            'E':{(Sr,Sc):(Sc+1)},
            'W':{(Sr,Sc):(Sc-1)}
    }
    print(Sr,Sc)
    print(inter['N'])
    print(inter['S'])
    print(inter['E'])
    print(inter['W'])
    print('')

    Srp, Scp = Sr, Sc
    for d in dirs:
        if d == 'N':
            Scp = Sc
            Sr = inter['N'][(Sr,Sc)]
            #Agregar del pasado
            inter['S'][(Sr,Sc)] = inter['S'][(Srp,Sc)]
            #Agregar casilla
            inter['N'][(Sr,Sc)] = inter['N'].get((Sr-1,Sc),Sr-1) 
            inter['E'][(Sr,Sc)] = inter['E'].get((Sr,Sc+1),Sc+1) 
            inter['W'][(Sr,Sc)] = inter['W'].get((Sr,Sc-1),Sc-1) 
            #Editar
            inter['N'][(Srp,Sc)] = inter['N'][(Sr,Sc)] 
            Srn = inter['N'][(Sr,Sc)]+1
            inter['S'][(Srn,Sc)] = inter['S'][(Srp,Sc)]

            Scr = inter['E'][(Sr,Sc)]-1
            Scl = inter['W'][(Sr,Sc)]+1
            inter['E'][(Sr,Scl)] = inter['E'][(Sr,Sc)]
            inter['W'][(Sr,Scr)] = inter['W'][(Sr,Sc)]
        elif d == 'S':
            Scp = Sc
            Sr = inter['S'][(Sr,Sc)]
            #Agregar del pasado
            inter['N'][(Sr,Sc)] = inter['N'][(Srp,Sc)]
            #Agregar casilla
            inter['S'][(Sr,Sc)] = inter['S'].get((Sr+1,Sc),Sr+1) 
            inter['E'][(Sr,Sc)] = inter['E'].get((Sr,Sc+1),Sc+1) 
            inter['W'][(Sr,Sc)] = inter['W'].get((Sr,Sc-1),Sc-1) 
            #Editar
            inter['S'][(Srp,Sc)] = inter['S'][(Sr,Sc)]
            Srn = inter['S'][(Sr,Sc)]-1
            inter['N'][(Srn,Sc)] = inter['N'][(Srp,Sc)]

            Scr = inter['E'][(Sr,Sc)]-1
            Scl = inter['W'][(Sr,Sc)]+1
            inter['E'][(Sr,Scl)] = inter['E'][(Sr,Sc)]
            inter['W'][(Sr,Scr)] = inter['W'][(Sr,Sc)]
        elif d == 'E':
            Srp = Sr
            Sc = inter['E'][(Sr,Sc)]
            #Agregar del pasado
            inter['W'][(Sr,Sc)] = inter['W'][(Sr,Scp)]
            #Agregar casilla
            inter['E'][(Sr,Sc)] = inter['E'].get((Sr,Sc+1),Sc+1) 
            inter['N'][(Sr,Sc)] = inter['N'].get((Sr-1,Sc),Sr-1) 
            inter['S'][(Sr,Sc)] = inter['S'].get((Sr+1,Sc),Sr+1) 
            #Editar
            inter['E'][(Sr,Scp)] = inter['E'][(Sr,Sc)]
            Scn = inter['E'][(Sr,Sc)]-1
            inter['W'][(Sr,Scn)] = inter['W'][(Sr,Scp)]
            
            Srd = inter['S'][(Sr,Sc)]-1
            Sru = inter['N'][(Sr,Sc)]+1
            inter['S'][(Sru,Sc)] = inter['S'][(Sr,Sc)]
            inter['N'][(Srd,Sc)] = inter['N'][(Sr,Sc)]
        elif d == 'W':
            Srp = Sr
            Sc = inter['W'][(Sr,Sc)]
            #Agregar del pasado
            inter['E'][(Sr,Sc)] = inter['E'][(Sr,Scp)]
            #Agregar casilla
            inter['W'][(Sr,Sc)] = inter['W'].get((Sr,Sc-1),Sc-1) 
            inter['N'][(Sr,Sc)] = inter['N'].get((Sr-1,Sc),Sr-1) 
            inter['S'][(Sr,Sc)] = inter['S'].get((Sr+1,Sc),Sr+1) 
            #Editar
            inter['W'][(Sr,Scp)] = inter['W'][(Sr,Sc)]
            Scn = inter['W'][(Sr,Sc)]+1
            inter['E'][(Sr,Scn)] = inter['E'][(Sr,Scp)]
            
            Srd = inter['S'][(Sr,Sc)]-1
            Sru = inter['N'][(Sr,Sc)]+1
            inter['S'][(Sru,Sc)] = inter['S'][(Sr,Sc)]
            inter['N'][(Srd,Sc)] = inter['N'][(Sr,Sc)]

        print(d,Sr,Sc)
        print(inter['N'])
        print(inter['S'])
        print(inter['E'])
        print(inter['W'])
        print('')

    print('Case #{}: {} {}'.format(t+1,Sr,Sc))

'''
5
5 3 6 2 3
EEWNS
4 3 3 1 1
SESE
11 5 8 3 4
NEESSWWNESE
15 7 3 2 2 
SESSWNWSSEENNWS
1
11 6 3 2 2     
SESSWNWSSEN
'''