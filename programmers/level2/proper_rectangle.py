import math


def solution(w, h):
    if w < h:
        w, h = h, w
    gcd = math.gcd(w, h)
    w_ = int(w/gcd)
    h_ = int(h/gcd)
    remain = w_ * h_ - (w_ + h_ - 1)
    total = remain * gcd + (w - w_) * h
    return total


if __name__ == "__main__":
    w, h = 8, 12
    print(solution(w, h))