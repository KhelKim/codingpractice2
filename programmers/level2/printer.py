from collections import deque


def solution(priorities, location):
    priorities = deque(priorities)
    locations = deque([i for i in range(len(priorities))])
    first_value = priorities[0]
    count = 0
    while priorities:
        if first_value < max(priorities):
            priorities.rotate(-1)
            locations.rotate(-1)
        else:
            priorities.popleft()
            candi = locations.popleft()
            count += 1
            if candi == location:
                break
        first_value = priorities[0]
    return count


if __name__ == "__main__":
    priorities, location = [1, 1, 9, 1, 1, 1], 0
    print(solution(priorities, location))
