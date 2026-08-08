from itertools import permutations

INF = float('inf')

def tsp(cost):
    n = len(cost)
    cities = list(range(1, n))

    best_cost = INF
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]

        total = 0

        for i in range(n):
            total += cost[path[i]][path[i + 1]]

        if total < best_cost:
            best_cost = total
            best_path = path

    return best_path, best_cost


cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

cities = ['A', 'B', 'C', 'D', 'E']

path, cost_value = tsp(cost)

print("Optimal Tour:", " -> ".join(cities[i] for i in path))
print("Minimum Cost:", cost_value)

print("\nPath verification:")

for i in range(len(path) - 1):
    u = path[i]
    v = path[i + 1]
    print(f"{cities[u]} -> {cities[v]}: cost = {cost[u][v]}")