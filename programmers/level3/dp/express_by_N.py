class DP(object):
    def __init__(self, N, number):
        self.N = N
        self.number = number
        self.memo = [[], [N]]
        self.visit = {N}

    def __call__(self):
        if self.number == self.N:
            return 1
        for _ in range(8):
            count = len(self.memo)

            new_number = int(str(self.N)*count)
            if self.number == new_number:
                return count
            self.memo.append([new_number])
            self.visit.add(new_number)

            for i in range(1, count):
                left_count = i
                right_count = count - i

                for left in self.memo[left_count]:
                    for right in self.memo[right_count]:
                        if right != 0:
                            candi = [left + right, left - right, left * right, left // right]
                        else:
                            candi = [left + right, left - right, left * right]

                        if self.number in candi:
                            return count
                        else:
                            for value in candi:
                                if value not in self.visit:
                                    self.memo[-1].append(value)
                                    self.visit.add(value)
        return -1


def solution(N, number):
    dp = DP(N, number)
    return dp()


if __name__ == "__main__":
    N, number = 5, 12
    print(solution(N, number))