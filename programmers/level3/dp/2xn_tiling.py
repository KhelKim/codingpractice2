def solution(n):
    a, b = 1, 2
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for _ in range(3, n+1):
            a, b = b, a + b
        return b % 1000000007


if __name__ == "__main__":
    n = int(10e10)
    print(solution(n))
