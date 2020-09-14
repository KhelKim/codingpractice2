class DFS(object):
    def __init__(self, numbers):
        self.numbers = numbers

    def __call__(self, depth=0, value=0):
        if depth == len(self.numbers):
            yield value
        else:
            for i in range(2):
                if i == 0:
                    yield from self(depth + 1, value+self.numbers[depth])
                else:
                    yield from self(depth + 1, value-self.numbers[depth])


def solution(numbers, target):
    count = 0
    dfs = DFS(numbers)
    for value in dfs():
        if value == target:
            count += 1
    return count


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    print(solution(numbers, 3))
