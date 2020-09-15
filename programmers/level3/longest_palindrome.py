def solution(s):
    for n_gram in range(len(s), 0, -1):
        for i in range(len(s)-n_gram+1):
            if s[i:i+n_gram] == s[i:i+n_gram][::-1]:
                return n_gram
