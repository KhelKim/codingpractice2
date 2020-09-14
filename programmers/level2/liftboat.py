from collections import deque


def solution(people, limit):
    people = deque(sorted(people))
    count = 0
    while people:
        if len(people) == 1:
            people.pop()
            count += 1
        else:
            light, heavy = people[0], people[-1]
            if light + heavy <= limit:
                people.pop(), people.popleft()
                count += 1
            else:
                people.pop()
                count += 1
    return count
