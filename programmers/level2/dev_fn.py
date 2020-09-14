import math
from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)

    result = []
    while progresses:
        count = 1
        base_progress = progresses.popleft()
        base_speed = speeds.popleft()

        base_remain = 100 - base_progress
        base_days = int(math.ceil(base_remain / base_speed))

        while progresses:
            next_progress = progresses[0]
            next_speed = speeds[0]

            if 100 <= next_progress + next_speed * base_days:
                (progresses.popleft(), speeds.popleft())
                count += 1
            else:
                break
        result.append(count)
    return result


if __name__ == "__main__":
    progresses = [93,30,55]
    speeds = [1,30,5]
    print(solution(progresses, speeds))
