def solution(n):
    memo = [[1, 3]]
    for _ in range(2, n + 1):
        new_memo = []
        for start, end in memo:
            if (start, end) == (1, 2):
                new_memo.append([1, 3])
            elif (start, end) == (1, 3):
                new_memo.append([1, 2])
            elif (start, end) == (2, 3):
                new_memo.append([3, 2])
            elif (start, end) == (2, 1):
                new_memo.append([3, 1])
            elif (start, end) == (3, 1):
                new_memo.append([2, 1])
            elif (start, end) == (3, 2):
                new_memo.append([2, 3])
        new_memo.append([1, 3])

        for start, end in memo:
            if (start, end) == (1, 2):
                new_memo.append([2, 1])
            elif (start, end) == (1, 3):
                new_memo.append([2, 3])
            elif (start, end) == (2, 3):
                new_memo.append([1, 3])
            elif (start, end) == (2, 1):
                new_memo.append([1, 2])
            elif (start, end) == (3, 1):
                new_memo.append([3, 2])
            elif (start, end) == (3, 2):
                new_memo.append([3, 1])
        memo = new_memo
    return memo


if __name__ == "__main__":
    for i in range(1, 5):
        n = i
        print(n)
        print(solution(n))