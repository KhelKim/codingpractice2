import math


def solution(n, k):
    numbers = [i+1 for i in range(n)]
    result = []
    k -= 1
    for i in range(n, 0, -1):
        f = math.factorial(i - 1)
        q, r = divmod(k, f)
        result.append(numbers.pop(q))
        k = r
    return result


if __name__ == "__main__":
    n, k = 3, 5
    print(solution(n, k))