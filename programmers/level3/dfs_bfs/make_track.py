from pprint import pprint
from collections import deque


class BFS(object):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.n = len(board)
        self.move = ((1, 0), (0, 1), (-1, 0), (0, -1))
        self.cost_board = [[int(1e10)] * self.n for _ in range(self.n)]
        self.cost_board[0][0] = 0
        self.queue = deque()

    def execute(self):
        self.queue.append((0, 0, 0, None, 0))  # x, y, depth, direction, cost
        while self.queue:
            x, y, depth, direction, cost = self.queue.popleft()
            for dx, dy in self.move:
                nx, ny = x + dx, y + dy

                if not self.check(nx, ny): continue

                change, new_direction = self.determine_direction(dx, dy, direction)
                if change is False:
                    if self.cost_board[nx][ny] >= cost + 100:
                        self.cost_board[nx][ny] = cost + 100
                        self.queue.append((nx, ny, depth + 1, new_direction, cost + 100))
                else:
                    if self.cost_board[nx][ny] >= cost + 600:
                        self.cost_board[nx][ny] = cost + 600
                        self.queue.append((nx, ny, depth + 1, new_direction, cost + 600))
        return self.cost_board[-1][-1]

    def check(self, nx, ny):
        if not 0 <= nx < self.n: return False
        if not 0 <= ny < self.n: return False
        if self.board[nx][ny] == 1: return False
        return True

    @staticmethod
    def determine_direction(dx, dy, direction):
        change = False
        if direction is None:
            if (dx, dy) in ((1, 0), (-1, 0)):
                direction = "vertical"
            else:
                direction = "horizontal"
        elif direction == "vertical":
            if (dx, dy) in ((1, 0), (-1, 0)):
                pass
            else:
                direction = "horizontal"
                change = True
        elif direction == "horizontal":
            if (dx, dy) in ((1, 0), (-1, 0)):
                direction = "vertical"
                change = True
            else:
                pass
        return change, direction


def solution(board):
    bfs = BFS(board)
    return bfs.execute()


if __name__ == "__main__":
    board = [[0,0,0],[0,0,0],[0,0,0]]
    print(solution(board))
