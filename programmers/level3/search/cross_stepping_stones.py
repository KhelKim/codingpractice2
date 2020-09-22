def get_n_submerge(stones, value):
    max_count = 0
    count = 0
    for v in stones:
        if v < value:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count
    return max_count


def solution(stones, k):
    start, end = 0, 200000000
    while start <= end:
        middle = (start + end) // 2
        n_submerge = get_n_submerge(stones, middle)
        if n_submerge < k:
            start, end = middle + 1, end
        elif n_submerge >= k:
            start, end = start, middle - 1
    middle = (start + end) // 2
    return middle



if __name__ == "__main__":
    # stones, k = [2, 4, 5, 4, 0, 0, 4, 4, 4, 4, 2, 5, 1], 3
    stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
    # stones, k = [1, 1, 1, 1, 1, 2], 2
    print(solution(stones, k))
    # print(get_n_submerge(stones, 4))
