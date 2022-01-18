# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef29

from heapq import *

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
    queue = {0}
    relevant_stones = set()
    while queue:
        stone = queue.pop()
        while queue and stone in relevant_stones:
            stone = queue.pop()
        if stone in relevant_stones:
            break

        relevant_stones.add(stone)
        for next_node in inverse_recipes.get(stone,set()):
            if next_node not in relevant_stones:
                queue.add(next_node)

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
        for node in seed_nodes[stone]:
            table[node][stone] = 0
    
    # Save the relevant recepies
    outs_recipe = {}
    for r in range(R):
        if base_outs[r] in relevant_stones:
            if recipes[r] in outs_recipe:
                outs_recipe[recipes[r]].append(base_outs[r])
            else:
                outs_recipe[recipes[r]] = [base_outs[r]]

    # Create priority queue
    hp = []
    order_map = {}
    past_sums = set()
    for i in range(N):
        for stone in relevant_stones:
            val = table[i][stone]
            if val in past_sums:
                order_map[val].add((i, stone))
            else:
                order_map[val] = {(i, stone)}
                past_sums.add(val)
                heappush(hp, val)
                
    # Create recipes_stones
    for r in range(R):
        if base_outs[r] in relevant_stones:
            for stone in recipes[r]:
                recipes_stone[stone].append(r)

    # Run the optimization
    while hp:
        val = hp[0]
        if len(order_map[val]) == 0:
            heappop(hp)
            del(order_map[val])
            continue
        else:
            node, curr_stone = order_map[val].pop()
        
        # Optimize with moving the stone
        for link_node in links[node]:
            if val+1 < table[link_node][curr_stone]:
                past_sum = table[link_node][curr_stone]
                order_map[past_sum].remove((link_node,curr_stone))
                table[link_node][curr_stone] = val+1
                if val+1 in past_sums:
                    order_map[val+1].add((link_node,curr_stone))
                else:
                    order_map[val+1] = {(link_node,curr_stone)}
                    past_sums.add(val+1)
                    heappush(hp, val+1)

        # Optimize with recipies
        for ind_recipe in recipes_stone[curr_stone]:
            sum_recipe = 0
            for sum_stone in recipes[ind_recipe]:
                sum_recipe += table[node][sum_stone]
            for out_stone in outs_recipe[recipes[ind_recipe]]:
                past_sum = table[node][out_stone]
                if sum_recipe < past_sum:
                    order_map[past_sum].remove((node,out_stone))
                    table[node][out_stone] = sum_recipe
                    if sum_recipe in past_sums:
                        order_map[sum_recipe].add((node,out_stone))
                    else:
                        order_map[sum_recipe] = {(node,out_stone)}
                        past_sums.add(sum_recipe)
                        heappush(hp, sum_recipe)

    ans = inf
    for i in range(N):
        ans = min(table[i][0], ans)
    if lmt < ans:
        ans = -1

    print("Case #{}: {}".format(t+1, ans))