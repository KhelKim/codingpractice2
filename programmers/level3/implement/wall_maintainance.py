from itertools import permutations


def solution(n, weak, dist):
    dist = sorted(dist, reverse=True)
    min_count = int(10e10)

    if dist[0] >= n-1:
        return 1

    for dist in permutations(dist):
        for idx in range(len(weak)):
            count = 0
            check = 0
            for d in dist:
                count += 1
                start = weak[idx]
                end = (start + d) % n
                while start < end and check < len(weak) and start <= weak[idx] <= end:
                    check += 1
                    idx = (idx + 1) % len(weak)
                while end < start and check < len(weak) and (start <= weak[idx] or weak[idx] <= end):
                    check += 1
                    idx = (idx + 1) % len(weak)
                if check >= len(weak):
                    break
            if min_count > count:
                min_count = count
    return min_count


if __name__ == "__main__":
    n, weak, dist = 12, [1, 3, 4, 9, 10], [3, 5, 7]
    print(solution(n, weak, dist))