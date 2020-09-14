from collections import deque


class DFS(object):
    def __init__(self, n, vertex):
        self.n = n
        self.vertex = vertex
        self.edges = self.make_edges()

    def make_edges(self):
        edges = {n+1: [] for n in range(self.n)}
        for start, end in self.vertex:
            edges[start].append(end)
            edges[end].append(start)
        return edges

    def __call__(self):
        visit = [False] * self.n
        queue = deque([(0, 1)])

        visit[0] = True
        max_depth = 0
        count = 1
        while queue:
            depth, c_node = queue.popleft()

            if max_depth < depth:
                count = 1
                max_depth = depth
            elif max_depth == depth:
                count += 1

            for node in self.edges[c_node]:
                if visit[node-1] is True: continue
                else:
                    visit[node-1] = True
                    queue.append((depth+1, node))
        return count


def solution(n, vertex):
    dfs = DFS(n, vertex)
    return dfs()


if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, vertex))