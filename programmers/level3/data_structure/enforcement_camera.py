from collections import deque


def solution(routes):
    routes = deque(sorted(routes, key=lambda x: x[1]))
    base_start, base_end = routes.popleft()
    count = 1
    while routes:
        start, end = routes.popleft()
        if base_end < start:
            count += 1
            base_end = end
    return count
