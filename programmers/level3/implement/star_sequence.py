from collections import Counter


def solution(a):
    counter = Counter(a)
    counter = counter.most_common()
    max_length = 0
    for core, count in counter:
        if count < max_length: continue

        last_idx = -2
        length = 0
        for i in range(len(a)-1):
            window = a[i:i+2]
            if window[0] == window[1]: continue
            if core not in window: continue
            if i - last_idx == 1: continue
            else:
                length += 2
                last_idx = i
        if max_length < length:
            max_length = length
    return max_length


if __name__ == "__main__":
    a = [0, 3, 3, 0, 7, 2, 0, 2, 2, 0]
    print(solution(a))
