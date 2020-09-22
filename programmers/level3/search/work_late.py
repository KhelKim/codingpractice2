def working_hours(middle, works, integral):
    return integral[middle] - works[middle] * (middle + 1)


def get_works_n_integral(works):
    works = sorted(works, reverse=True)
    i, integral = 0, []
    for w in works:
        i += w
        integral.append(i)
    return works, integral


def bisection_search(n, works, integral):
    start, end = 0, len(works) - 1
    while start <= end:
        middle = (start + end) // 2
        hours = working_hours(middle, works, integral)
        if hours < n:
            start, end = middle + 1, end
        elif hours > n:
            start, end = start, middle - 1
        else:
            break
    middle = (start + end) // 2
    return middle


def get_result(works):
    result = 0
    for w in works:
        if w <= 0:
            continue
        else:
            result += w * w
    return result


def solution(n, works):
    works, integral = get_works_n_integral(works)
    middle = bisection_search(n, works, integral)
    hours = working_hours(middle, works, integral)
    remain = n - hours
    q, r = divmod(remain, middle+1)
    works[:r] = [works[middle] - (q + 1)] * r
    works[r:middle+1] = [works[middle] - q] * (middle + 1 - r)
    return get_result(works)


if __name__ == "__main__":
    # n, works = 7, [4, 3, 3, 10, 12]
    # n, works = 1000000, [50000 for _ in range(20000)]
    # n, works = 1, [2, 1, 2]
    n, works = 3, [1, 1]

    print(solution(n, works))
