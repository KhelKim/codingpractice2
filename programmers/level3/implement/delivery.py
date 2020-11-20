def solution(N, road, K):
    inf = K + 1
    dic = {i+1: {} for i in range(N)}
    for start, end, cost in road:
        if end not in dic[start]:
            dic[start][end] = inf
        if start not in dic[end]:
            dic[end][start] = inf

        dic[start][end] = cost if cost < dic[start][end] else dic[start][end]
        dic[end][start] = cost if cost < dic[start][end] else dic[start][end]

    visit = []
    check = [False] * (N+1)

    check[1] = True
    new = (1, 0)
    while new is not None:
        visit.append(new)
        new = None
        min_cost = inf
        for start, seed_cost in visit:
            for end, new_cost in dic[start].items():
                cost = seed_cost + new_cost

                if check[end] is True: continue
                if cost > K: continue
                if cost >= min_cost: continue

                min_cost = cost
                new = (end, cost)
        if new is not None:
            check[new[0]] = True

    return len(visit)


if __name__ == "__main__":
    N, road, K = 5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
                     [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3
    print(solution(N, road, K))
