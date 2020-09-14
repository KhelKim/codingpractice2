def solution(m, n, puddles):
    memo = [[0] * m for _ in range(n)]
    puddles_hash = set([(y-1, x-1) for x, y in puddles])
    for x in range(n):
        if (x, 0) not in puddles_hash:
            memo[x][0] = 1
        else:
            break
    for y in range(m):
        if (0, y) not in puddles_hash:
            memo[0][y] = 1
        else:
            break
    print(memo)
    for x in range(1, n):
        for y in range(1, m):
            if (x, y) not in puddles_hash:
                memo[x][y] = memo[x-1][y] + memo[x][y-1]
    print(memo)
    return memo[-1][-1] % 1000000007


if __name__ == "__main__":
    m, n, puddles = 4, 3, [[2, 1]]
    print(solution(m, n, puddles))
