from collections import deque


class BFS(object):
    def __init__(self, board):
        self.board = board
        self.n = len(board)
        self.loc = ((0, 0), (0, 1))
        self.visit = set()
        self.visit.add(self.loc)

    def __call__(self):
        queue = deque([(self.loc, 0)])
        move1 = ((1, 0), (0, 1), (-1, 0), (0, -1))
        move2 = ("fpsu", "fpsd", "spfu", "spfd")  # horizon, f-first p-pivot s-second l-left r-right
        move3 = ("fpsl", "fpsr", "spfl", "spfr")  # vertical, u-up d-down

        while queue:
            ((cx1, cy1), (cx2, cy2)), depth = queue.popleft()
            for move in move1:
                if self.check1(cx1, cy1, cx2, cy2, move):
                    dx, dy = move
                    nx1, ny1, nx2, ny2 = cx1+dx, cy1+dy, cx2+dx, cy2+dy
                    if nx2 == ny2 == (self.n - 1): return depth + 1
                    queue.append((((nx1, ny1), (nx2, ny2)), depth+1))
                    self.visit.add(((nx1, ny1), (nx2, ny2)))
            if cx1 == cx2:
                for move in move2:
                    if self.check2(cx1, cy1, cx2, cy2, move):
                        (nx1, ny1), (nx2, ny2) = self.get_loc_move2(cx1, cy1, cx2, cy2, move)
                        if nx2 == ny2 == (self.n - 1): return depth + 1
                        queue.append((((nx1, ny1), (nx2, ny2)), depth + 1))
                        self.visit.add(((nx1, ny1), (nx2, ny2)))
            if cy1 == cy2:
                for move in move3:
                    if self.check3(cx1, cy1, cx2, cy2, move):
                        (nx1, ny1), (nx2, ny2) = self.get_loc_move3(cx1, cy1, cx2, cy2, move)
                        if nx2 == ny2 == (self.n - 1): return depth + 1
                        queue.append((((nx1, ny1), (nx2, ny2)), depth + 1))
                        self.visit.add(((nx1, ny1), (nx2, ny2)))

    def check1(self, cx1, cy1, cx2, cy2, move):
        dx, dy = move
        nx1, ny1, nx2, ny2 = cx1 + dx, cy1 + dy, cx2 + dx, cy2 + dy
        if not 0 <= nx1 < self.n: return False
        if not 0 <= ny1 < self.n: return False
        if not 0 <= nx2 < self.n: return False
        if not 0 <= ny2 < self.n: return False
        if self.board[nx1][ny1] == 1: return False
        if self.board[nx2][ny2] == 1: return False
        if ((nx1, ny1), (nx2, ny2)) in self.visit: return False
        return True

    def check2(self, cx1, cy1, cx2, cy2, move):
        (nx1, ny1), (nx2, ny2) = self.get_loc_move2(cx1, cy1, cx2, cy2, move)
        if move in ["fpsd", 'spfd']:
            if not 0 <= nx1 < self.n: return False
            if not 0 <= ny1 < self.n: return False
            if not 0 <= nx2 < self.n: return False
            if not 0 <= ny2 < self.n: return False
            if self.board[cx1+1][cy1] == 1: return False
            if self.board[cx2+1][cy2] == 1: return False
            if ((nx1, ny1), (nx2, ny2)) in self.visit: return False
        elif move in ["fpsu", "spfu"]:
            if not 0 <= nx1 < self.n: return False
            if not 0 <= ny1 < self.n: return False
            if not 0 <= nx2 < self.n: return False
            if not 0 <= ny2 < self.n: return False
            if self.board[cx1 - 1][cy1] == 1: return False
            if self.board[cx2 - 1][cy2] == 1: return False
            if ((nx1, ny1), (nx2, ny2)) in self.visit: return False
        return True

    def check3(self, cx1, cy1, cx2, cy2, move):
        (nx1, ny1), (nx2, ny2) = self.get_loc_move3(cx1, cy1, cx2, cy2, move)
        if move in ["fpsl", "spfl"]:
            if not 0 <= nx1 < self.n: return False
            if not 0 <= ny1 < self.n: return False
            if not 0 <= nx2 < self.n: return False
            if not 0 <= ny2 < self.n: return False
            if self.board[cx1][cy1-1] == 1: return False
            if self.board[cx2][cy2-1] == 1: return False
            if ((nx1, ny1), (nx2, ny2)) in self.visit: return False

        elif move in ["fpsr", "spfr"]:
            if not 0 <= nx1 < self.n: return False
            if not 0 <= ny1 < self.n: return False
            if not 0 <= nx2 < self.n: return False
            if not 0 <= ny2 < self.n: return False
            if self.board[cx1][cy1+1] == 1: return False
            if self.board[cx2][cy2+1] == 1: return False
            if ((nx1, ny1), (nx2, ny2)) in self.visit: return False
        return True

    @staticmethod
    def get_loc_move2(cx1, cy1, cx2, cy2, move):
        if move == "fpsu":
            return (cx2-1, cy2-1), (cx1, cy1)
        elif move == "fpsd":
            return (cx1, cy1), (cx2+1, cy2-1)
        elif move == "spfu":
            return (cx1-1, cy1+1), (cx2, cy2)
        elif move == "spfd":
            return (cx2, cy2), (cx1+1, cy1+1)

    @staticmethod
    def get_loc_move3(cx1, cy1, cx2, cy2, move):
        if move == "fpsl":
            return (cx2-1, cy2-1), (cx1, cy1)
        elif move == "fpsr":
            return (cx1, cy1), (cx2-1, cy2+1)
        elif move == "spfl":
            return (cx1+1, cy1-1), (cx2, cy2)
        elif move == "spfr":
            return (cx2, cy2), (cx1+1, cy1+1)


def solution(board):
    bfs = BFS(board)
    return bfs()


if __name__ == "__main__":
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    print(solution(board))