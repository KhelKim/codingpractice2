class DFS(object):
    def __init__(self, numbers):
        self.numbers = numbers
        self.visit = {}
        self.checks = [False] * len(numbers)
        self.route = []

    def __call__(self):
        string_route = "".join(self.route)
        if string_route:
            yield string_route

        for i, num in enumerate(self.numbers):
            current_route = string_route + num
            if self.checks[i] is True: continue
            if current_route in self.visit: continue
            self.route.append(num)
            self.visit[current_route] = True
            self.checks[i] = True

            yield from self()

            self.route.pop()
            self.checks[i] = False


def is_prime(number):
    if number > 1:
        for i in range(2, number//2+1):
            if number % i == 0:
                return False
        return True
    else:
        return False


def solution(numbers):
    dfs = DFS(numbers)
    prime_set = set()
    for i in dfs():
        number = int(i)
        if is_prime(number):
            prime_set.add(number)
    return len(prime_set)


if __name__ == "__main__":
    print(is_prime(11))
