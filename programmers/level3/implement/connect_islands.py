def solution(n, costs):
    INF = int(10e10)
    check_list = [False] * n
    edges = {i: [] for i in range(n)}
    for start, end, cost in costs:
        edges[start].append((end, cost))
        edges[end].append((start, cost))

    connected_islands = [0]
    check_list[0] = True
    total_value = 0
    for _ in range(n-1):
        min_value = INF
        next_island = 0
        for island in connected_islands:
            for target, cost in edges[island]:
                if check_list[target] is False and cost < min_value:
                    min_value = cost
                    next_island = target
        connected_islands.append(next_island)
        check_list[next_island] = True
        total_value += min_value
    return total_value


if __name__ == "__main__":
    n = 4
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n, costs))