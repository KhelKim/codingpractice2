def solution(dirs):
    directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    visit = set()
    nx, ny = 0, 0
    for direction in dirs:
        dx, dy = directions[direction]
        cx, cy = nx + dx, ny + dy
        if not -5 <= cx <= 5: continue
        if not -5 <= cy <= 5: continue
        visit.add(tuple(sorted([(nx, ny), (cx, cy)])))
        nx, ny = cx, cy
    return len(visit)


