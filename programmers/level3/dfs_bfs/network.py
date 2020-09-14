class DFS(object):
    def __init__(self, n, computers):
        self.n = n
        self.computers = computers
        self.visit = set()
        self.n_networks = 0

    def __call__(self):
        for i in range(self.n):
            if i in self.visit: continue
            else:
                self.n_networks += 1
                self.visit.add(i)
                self.dfs(i)
        return self.n_networks

    def dfs(self, node):
        for i, is_connected in enumerate(self.computers[node]):
            if is_connected == 0: continue
            if i == node: continue
            if i in self.visit: continue
            else:
                self.visit.add(i)
                self.dfs(i)


def solution(n, computers):
    dfs = DFS(n, computers)
    return dfs()


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))
