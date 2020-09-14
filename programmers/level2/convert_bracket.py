def check_bracket(p):
    stack = []
    for char in p:
        if char == "(":
            stack.append(char)
        elif stack and char == ")":
            stack.pop()
        else:
            return False
    return True


def divide_u_v(p):
    dic = {"(": 0, ")": 0}
    u = []
    for i, char in enumerate(p):
        u.append(char)
        dic[char] += 1
        if dic["("] == dic[")"]:
            u = "".join(u)
            v = p[i+1:]
            return u, v
    raise AssertionError()


def solution(p):
    if not p:
        return p
    else:
        u, v = divide_u_v(p)
        if check_bracket(u):
            return u + solution(v)
        else:
            tmp = "(" + solution(v) + ")"
            tmp += "".join(["(" if char == ")" else ")" for char in u[1:-1]])
            return tmp


if __name__ == "__main__":
    p = "()))((()"
    # print(check_bracket(p))
    print(solution(p))
