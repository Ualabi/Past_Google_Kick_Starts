# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef29

from heapq import *

def Table(tb):
    ans = ""
    for row in tb:
        aux = ""
        for cell in row:
            word = str(row[cell])
            aux += " "*(5-len(word))+word
        ans += aux + "\n"
    return ans + "\n"

kkk = []
ppp = []
lmt = 10**12
T = int(input())
for t in range(T):
    N, M, S, R = map(int, input().split())
    
    # Create links between the cities
    links = [set() for _ in range(N)]
    for m in range(M):
        a = list(map(int, input().split()))
        links[a[0]-1].add(a[1]-1)
        links[a[1]-1].add(a[0]-1)

    # Create the table and map the cities where the stones are
    inf = float('inf')
    stones = [set() for _ in range(S)]
    for n in range(N):
        a = list(map(int,input().split()))
        b = []
        for i in range(a[0]):
            b.append(a[i+1]-1)
            stones[a[i+1]-1].add(n)

    # Save the base recepies
    inverse_recipes = {}
    recipes, base_outs = [], []
    for r in range(R):
        a = list(map(int,input().split()))
        b = []
        for i in range(a[0]):
            b.append(a[i+1]-1)
        c = tuple(sorted(b))
        out_stone = a[-1]-1
        recipes.append(c)
        base_outs.append(out_stone)
        inverse_recipes[out_stone] = inverse_recipes.get(out_stone, set()) | set(b)

    # Get the relevant stones
    order = []
    queue = [0]
    relevant_stones = set()
    while queue:
        new_queue = []
        for stone in queue:
            order.append(stone)
            relevant_stones.add(stone)
            for next_node in inverse_recipes.get(stone,set()):
                if next_node not in relevant_stones:
                    new_queue.append(next_node)
        queue = new_queue

    # Get the relevant nodes with their stones
    recipes_stone = {}
    seed_nodes = [set() for _ in range(S)]
    for stone in relevant_stones:
        recipes_stone[stone] = []
        for ind in stones[stone]:
            seed_nodes[stone].add(ind)

    # Propagate the seed nodes
    table = [{i:inf for i in relevant_stones} for _ in range(N)]
    for stone in relevant_stones:
        lvl = 0
        queue = seed_nodes[stone]
        while queue:
            new_queue = set()
            for node in queue:
                if table[node][stone] == inf:
                    table[node][stone] = lvl
                    new_queue |= links[node]
            queue = new_queue
            lvl += 1
    
    # Save the relevant recepies
    outs_recipe = {}
    for r in range(R):
        if base_outs[r] in relevant_stones:
            if recipes[r] in outs_recipe:
                outs_recipe[recipes[r]].append(base_outs[r])
            else:
                outs_recipe[recipes[r]] = [base_outs[r]]
    # print()
    # print(relevant_stones)
    # print(outs_recipe)
    # print()
    print(Table(table))

    # Create missing 
    hp = []
    order_map = {}
    past_sums = set()
    for i in range(N):
        for stone in (relevant_stones-{0}):
            val = table[i][stone]
            if val in past_sums:
                order_map[val].add((i, stone))
            else:
                order_map[val] = {(i, stone)}
                past_sums.add(val)
                heappush(hp, val)
    print(hp)
    # Create recipes_stones
    for r in range(R):
        if base_outs[r] in relevant_stones:
            for stone in recipes[r]:
                recipes_stone[stone].append(r)

    # for m in order_map:
    #     print(m,order_map[m])
    # print()
    
    # for stone in recipes_stone:
    #     print(stone, recipes_stone[stone])
    # print()

    # print(hp)
    # Run the optimization
    while hp:
        val = hp[0]
        if len(order_map[val]) == 0:
            heappop(hp)
            del(order_map[val])
            continue
        elif len(order_map[val]) == 1:
            heappop(hp)
            del(order_map[val])
        else:
            node, curr_stone = order_map[val].pop()

        print('<>', node, curr_stone, hp)
        print(Table(table))
        for ind_recipe in recipes_stone[curr_stone]:
            # print('<>', node, curr_stone, recipes[ind_recipe], outs_recipe[recipes[ind_recipe]])
            sum_recipe = 0
            for sum_stone in recipes[ind_recipe]:
                sum_recipe += table[node][sum_stone]
            for out_stone in outs_recipe[recipes[ind_recipe]]:
                if sum_recipe < table[node][out_stone]:
                    #print('->',node,out_stone)
                    past_sum = table[node][out_stone]
                    if past_sum < inf:
                        order_map[past_sum].remove((node,out_stone))
                        
                    table[node][out_stone] = sum_recipe
                    if sum_recipe in past_sums:
                        order_map[sum_recipe].add((node,out_stone))
                    else:
                        order_map[sum_recipe] = {(node,out_stone)}
                        past_sums.add(sum_recipe)
                        heappush(hp, sum_recipe)

                    sum_recipe += 1                    
                    propagation = links[node]
                    for link_node in propagation:
                        if sum_recipe < table[link_node][out_stone]:
                            # print(link_node,out_stone)
                            past_sum = table[link_node][out_stone]
                            if past_sum < inf:
                                order_map[past_sum].remove((link_node,out_stone))
                            table[link_node][out_stone] = sum_recipe
                            if sum_recipe in past_sums:
                                order_map[sum_recipe].add((link_node,out_stone))
                            else:
                                order_map[sum_recipe] = {(link_node,out_stone)}
                                past_sums.add(sum_recipe)
                                heappush(hp, sum_recipe)

    # print()
    # print(Table(table))

    ans = inf
    for i in range(N):
        ans = min(table[i][0], ans)
    if lmt < ans:
        ans = -1

    print("Case #{}: {}".format(t+1, ans))
    kkk.append("Case #{}: {}".format(t+1, ans))

for k in kkk:
    print(k)
print(ppp)