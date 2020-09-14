import heapq


def solution(operations):
    heap = []
    for operation in operations:
        oper, value = operation.split()
        value = int(value)
        if oper == "I":
            heapq.heappush(heap, value)
        else:
            if heap:
                if value == 1:
                    idx, max_v = 0, int(-10e10)
                    for i, v in enumerate(heap):
                        if max_v < v:
                            idx, max_v = i, v
                    heap.pop(idx)
                    heapq.heapify(heap)
                else:
                    heapq.heappop(heap)
    return [0, 0] if not heap else [max(heap), heap[0]]
