import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville and scoville[0] < K:
        if len(scoville) < 2:
            return -1
        count += 1
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)
        new = first_min + second_min * 2
        heapq.heappush(scoville, new)
    return count


if __name__ == "__main__":
    scoville = [1, 2]
    K = 7
    print(solution(scoville, K))
