class DFS(object):
    def __init__(self, n):
        self.n = n
        self.on_board = []
        self.count = 0
        self.diagonal_moves = ((-1, -1), (-1, 1))

    def check_possible(self, x, y):
        for tx, ty in self.on_board:
            dx, dy = tx - x, ty - y
            if dy == 0:
                return False
            else:
                if abs(dx) == abs(dy):
                    return False
        return True

    def execute(self, x=0):
        if x == self.n:
            self.count += 1
        else:
            for y in range(self.n):
                if self.check_possible(x, y):
                    self.on_board.append((x, y))
                    self.execute(x+1)
                    self.on_board.pop()


def solution(n):
    dfs = DFS(n)
    dfs.execute()
    return dfs.count


if __name__ == "__main__":
    for i in range(4, 13):
        print(solution(i))

