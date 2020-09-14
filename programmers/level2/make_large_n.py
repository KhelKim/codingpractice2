def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)


if __name__ == "__main__":
    number = "811188"
    k = 1
    print(solution(number, k))