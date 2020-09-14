def solution(genres, plays):
    counter = {}
    for genre, play in zip(genres, plays):
        if genre in counter:
            counter[genre] += play
        else:
            counter[genre] = play

    songs = [[i, genre, play, counter[genre]] for i, (genre, play) in enumerate(zip(genres, plays))]
    songs = sorted(songs, key=lambda x: (-x[3], -x[2], -x[0]))

    result, c_genre, c_count = [], "", 0
    for i, genre, _, _ in songs:
        if genre != c_genre:
            result.append(i)
            c_genre, c_count = genre, 1
        else:
            if c_count < 2:
                result.append(i)
                c_count = 2
    return result


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop", "A"]
    plays = [500, 600, 150, 800, 2500, 100000000]
    print(solution(genres, plays))
