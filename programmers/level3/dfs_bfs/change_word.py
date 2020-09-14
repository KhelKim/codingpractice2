from collections import deque
from itertools import combinations


class BFS(object):
    @staticmethod
    def is_convertible(word1, word2):
        count = 0
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                count += 1
            if count > 1:
                return False
        return True

    def make_edges(self, words):
        edges = {word: [] for word in words}
        for word1, word2 in combinations(words, 2):
            if self.is_convertible(word1, word2):
                edges[word1].append(word2)
                edges[word2].append(word1)
        return edges

    def __init__(self, begin, target, words):
        self.begin = begin
        self.target = target
        self.words = words if begin in words else (words + [begin])
        self.edges = self.make_edges(self.words)

    def __call__(self):
        queue = deque([(self.begin, 0)])
        visit = {word: False for word in self.words}
        while queue:
            current, depth = queue.popleft()
            visit[current] = True

            for word in self.edges[current]:
                if visit[word] is True: continue
                elif word == self.target: return depth + 1
                else: queue.append((word, depth+1))
        return 0


def solution(begin, target, words):
    bfs = BFS(begin, target, words)
    return bfs()


if __name__ == "__main__":
    begin = 'hit'
    target = 'cog'
    words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    print(solution(begin, target, words))
