def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    now = sorted_phone_book[0]
    for phone_number in sorted_phone_book[1:]:
        n = len(now)
        if now == phone_number[:n]:
            return False
        else:
            now = phone_number
    return True


if __name__ == "__main__":
    phone_book = ["119", "123", "97674223", "1195524421"]
    phone_book = ["123", "456", "789"]
    # phone_book = ["12", "123", "1235", "567", "88"]
    print(solution(phone_book))
