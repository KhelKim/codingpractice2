def solution(triangle):
    prev = [0]
    for i in range(len(triangle)):
        now = [0] * len(triangle[i])
        for j in range(len(triangle[i])):
            if j == 0:
                now[j] = triangle[i][j] + prev[0]
            elif j == len(triangle[i]) - 1:
                now[j] = triangle[i][j] + prev[-1]
            else:
                now[j] = max(triangle[i][j]+prev[j-1], triangle[i][j]+prev[j])
        prev = now
    return max(now)
