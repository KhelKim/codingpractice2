def solution(citations):
    citations.append(0)
    sorted_citations = sorted(citations, reverse=True)
    for i, citation in enumerate(sorted_citations[:-1]):
        count = i + 1
        if citation >= count >= sorted_citations[i+1]:
            return count
    return 0


if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    citations = [1, 1, 1, 1, 1]
    citations = [0, 0, 0, 0]
    print(solution(citations))
