from collections import deque


class DFS(object):
    def __init__(self, tickets):
        self.tickets = tickets
        self.n_tickets = len(tickets)
        self.edges = self.make_edges()
        self.route = ["ICN"]
        self.depth = 0

    def make_edges(self):
        edges = {}
        for start, end in self.tickets:
            if start not in edges:
                edges[start] = [[end, False]]
            else:
                edges[start].append([end, False])
            if end not in edges:
                edges[end] = []
        edges = {key: deque(sorted(value)) for key, value in edges.items()}
        return edges

    def __call__(self):
        if self.depth == self.n_tickets:
            yield self.route
        else:
            for idx, (node, is_used) in enumerate(self.edges[self.route[-1]]):
                if is_used: continue
                self.route.append(node)
                self.edges[self.route[-2]][idx][1] = True
                self.depth += 1
                yield from self()
                self.depth -= 1
                self.edges[self.route[-2]][idx][1] = False
                self.route.pop()


def solution(tickets):
    dfs = DFS(tickets)
    return next(dfs())


if __name__ == "__main__":
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    print(solution(tickets))
