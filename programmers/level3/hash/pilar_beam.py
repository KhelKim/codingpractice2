def check(board):
    for tmp in board:
        x, y, a = tmp
        if a == 0:  # 기둥
            if y == 0: continue
            elif (x, y, 1) in board or (x-1, y, 1) in board: continue
            elif (x, y-1, 0) in board: continue
            return False
        else:
            if (x, y-1, 0) in board or (x+1, y-1, 0) in board: continue
            elif (x-1, y, 1) in board and (x+1, y, 1) in board: continue
            return False
    return True


def solution(n, build_frame):
    board = set()
    for x, y, a, b in build_frame:
        if b == 0:
            board.remove((x, y, a))
            if not check(board):
                board.add((x, y, a))
        else:
            board.add((x, y, a))
            if not check(board):
                board.remove((x, y, a))
    return [list(l) for l in sorted(board)]


if __name__ == "__main__":
    n, build_frame = 5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
    print(solution(n, build_frame))