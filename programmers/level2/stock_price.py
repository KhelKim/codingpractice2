def solution(prices):
    result = [len(prices) - 1 - i for i in range(len(prices))]
    stack = []
    for idx, price in enumerate(prices):
        if not stack:
            stack.append((idx, price))
        else:
            while stack:
                last_idx, last_price = stack[-1]
                if price < last_price:
                    result[last_idx] = idx - last_idx
                    stack.pop()
                else:
                    break
            stack.append((idx, price))
    return result


if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))
