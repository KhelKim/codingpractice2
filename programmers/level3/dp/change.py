def solution(n, money):
    counter = [0] * (n+1)
    counter[0] = 1
    for m in money:
        for i in range(n+1):
            counter[i] = counter[i] if i < m else counter[i] + counter[i-m]
    return counter[-1] % 1000000007


if __name__ == "__main__":
    # n, money = 6, [i for i in range(1, 3)]
    # n, money = 5, [1, 2, 5]
    n, money = 100000, [i for i in range(1, 100)]
    print(solution(n, money))
