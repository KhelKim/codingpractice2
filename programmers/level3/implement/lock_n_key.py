from copy import deepcopy


def pad(square, m):
    n = len(square)
    size = n + 2 * m
    padded_square = [[0] * size for _ in range(size)]
    for dx in range(n):
        padded_square[m+dx][m:m+n] = square[dx][:]
    return padded_square


def rotate_90(square):
    rotated_matrix = []
    for column in zip(*square):
        reversed_column = column[::-1]
        rotated_matrix.append(reversed_column)
    return rotated_matrix


def checker(square, m, n):
    for dx in range(n):
        for dy in range(n):
            if square[m-1 + dx][m-1 + dy] != 1:
                return False
    return True


def fit(key, lock, i, j, m, n):
    tmp_lock = deepcopy(lock)
    for dx in range(m):
        for dy in range(m):
            tmp_lock[i+dx][j+dy] += key[dx][dy]
    if checker(tmp_lock, m, n):
        return True
    else:
        return False


def solution(key, lock):
    m, n = len(key), len(lock)
    pad_size = m - 1
    padded_lock = pad(lock, pad_size)
    total_size = len(padded_lock)

    for _ in range(4):
        key = rotate_90(key)
        for i in range(total_size-pad_size):
            for j in range(total_size-pad_size):
                if fit(key, padded_lock, i, j, m, n):
                    return True
    return False


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
