def solution(n):
    result = []
    num = "124"
    while n:
        n, r = divmod(n-1, 3)
        result.append(num[r])
    return "".join(result[::-1])
