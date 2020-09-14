def compress_s(s, length):
    init_str = s[:length]
    string = [(1, init_str)]
    for start in range(length, len(s), length):
        now = s[start:start+length]
        last_count, last_str = string[-1]
        if now == last_str:
            string[-1] = (last_count+1, last_str)
        else:
            string.append((1, now))
    result = "".join([str(count)+string if count > 1 else string for count, string in string])
    return result


def solution(s):
    max_lengths = len(s) // 2
    minimum = len(s)
    for i in range(1, max_lengths+1):
        result = compress_s(s, i)
        value = len(result)
        if value < minimum:
            minimum = value
    return minimum


if __name__ == "__main__":
    s = "aabbaccc"
    print(solution(s))
