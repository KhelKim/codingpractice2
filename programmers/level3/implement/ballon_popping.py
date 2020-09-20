def solution(a):
    min_value = int(10e20)
    idx = -1
    for i, v in enumerate(a):
        if min_value >= v:
            idx, min_value = i, v

    count = 0
    now_value = a[0]
    for v in a[:idx]:
        if v <= now_value:
            count += 1
            now_value = v
    now_value = a[-1]
    for v in a[idx:][::-1]:
        if v <= now_value:
            count += 1
            now_value = v
    return count


if __name__ == "__main__":
    ballons = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
    # ballons = [9, -1, -5]
    print(solution(ballons))