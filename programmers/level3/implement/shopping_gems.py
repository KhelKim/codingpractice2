from collections import deque


def solution(gems):
    n = len(gems)
    gem_counter = {gem: 0 for gem in gems}
    n_types = len(gem_counter)

    interval = []  # tuple : (length, start, end))
    start, end = 0, 1
    bought = deque(gems[start:end])
    bought_type = set(bought)
    gem_counter[bought[0]] += 1
    while start < n:
        if start == end:
            gem = gems[end]
            bought.append(gem)
            gem_counter[gem] += 1
            bought_type.add(gem)
            end += 1
        else:
            if len(bought_type) == n_types:
                interval.append([end-start, start, end])

                gem = bought.popleft()
                gem_counter[gem] -= 1
                if not gem_counter[gem]:
                    bought_type.remove(gem)
                start += 1
            elif end == n:
                gem = bought.popleft()
                gem_counter[gem] -= 1
                if not gem_counter[gem]:
                    bought_type.remove(gem)
                start += 1
            else:
                gem = gems[end]
                bought.append(gem)
                gem_counter[gem] += 1
                bought_type.add(gem)
                end += 1
    interval = sorted(interval)
    answer = interval[0]
    return [answer[1]+1, answer[2]]


if __name__ == "__main__":
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    # gems = ["AA", "AB", "AC", "AA", "AC"]
    # gems = ["XYZ", "XYZ", "XYZ"]
    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(gems))
