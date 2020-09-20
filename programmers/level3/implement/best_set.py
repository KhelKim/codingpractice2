def solution(n, s):
    if s < n:
        return [-1]
    else:
        q, r = divmod(s, n)
        result = [q] * n
        result[-r:] = [q+1] * r
        return result
