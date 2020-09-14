ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N_ALPHA = len(ALPHA)


def solution(name):
    name = list(name)
    display = ["A"] * len(name)
    n = len(name)
    location = 0
    count = 0
    while name != display:
        # vertical
        for i in range(0, N_ALPHA):
            if name[location] == ALPHA[i]:
                break
        for j in range(-1, -N_ALPHA-1, -1):
            if name[location] == ALPHA[j]:
                j = -j
                break
        display[location] = name[location]
        count += min(i, j)

        # horizontal
        for i in range(0, n):
            abs_loc_i = (location + i) % n
            if name[abs_loc_i] != display[abs_loc_i]:
                break
        else:
            return count
        for j in range(-1, -n-1, -1):
            abs_loc_j = (location + j) % n
            if name[abs_loc_j] != display[abs_loc_j]:
                j = -j
                break
        if i <= j:
            count += i
            location = abs_loc_i
        else:
            count += j
            location = abs_loc_j
    return count


if __name__ == "__main__":
    name = "JAN"
    print(solution(name))
