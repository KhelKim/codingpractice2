from copy import deepcopy


def make_edges(n, results):
    edges = {i+1: {"over": set(), "under": set()} for i in range(n)}
    for win, lose in results:
        edges[win]['over'].add(lose)
        edges[lose]['under'].add(win)
    return edges


def solution(n, results):
    edges = make_edges(n, results)
    origin = {}
    while edges != origin:
        origin = deepcopy(edges)
        for i in range(n):
            now = i + 1
            for j in range(n):
                target = j + 1

                if target in edges[now]['over']:
                    edges[now]['over'] = edges[now]['over'].union(edges[target]['over'])

                if target in edges[now]['under']:
                    edges[now]['under'] = edges[now]['under'].union(edges[target]['under'])

    count = 0
    for value in edges.values():
        if len(value['over']) + len(value['under']) == n - 1:
            count += 1
    return count


if __name__ == "__main__":
    n = 5

    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))