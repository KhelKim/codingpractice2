def solution(n, times):
    start_time, end_time = 1, 1000000000*100000
    middle_time = (start_time + end_time) // 2
    while start_time <= end_time:
        processed_people = 0
        remainder = 0
        for time in times:
            q, r = divmod(middle_time, time)
            processed_people += q
            remainder += r

        if processed_people < n:
            start_time, end_time = middle_time+1, end_time
        elif processed_people > n:
            start_time, end_time = start_time, middle_time-1
        else:
            if remainder != 0:
                start_time, end_time = start_time, middle_time-1
            else:
                return middle_time
        middle_time = (start_time + end_time) // 2
    return end_time+1


if __name__ == "__main__":
    n = 5
    times = [2, 3, 6]
    print(solution(n, times))
