import heapq
from collections import deque


def solution(jobs):
    n_jobs = len(jobs)
    jobs = [job[::-1] for job in jobs]
    jobs = deque(sorted(jobs, key=lambda x: (x[1], x[0])))
    current_time, sum_time, heap = 0, 0, []
    while jobs or heap:
        while jobs:
            processing_time, request_time = jobs[0]
            if request_time <= current_time:
                heapq.heappush(heap, jobs.popleft())
            else:
                break
        if not heap:
            processing_time, request_time = jobs.popleft()
            current_time = processing_time + request_time
        else:
            processing_time, request_time = heapq.heappop(heap)
            current_time += processing_time
        sum_time += current_time - request_time

    return int(sum_time/n_jobs)


if __name__ == "__main__":
    jobs = [[0, 3], [2, 9], [2, 6]]
    print(solution(jobs))
