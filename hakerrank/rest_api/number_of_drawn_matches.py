import requests


def getNumDraws(year):
    base = "https://jsonmock.hackerrank.com/api/football_matches"
    count = 0
    for score in range(11):
        url = f"{base}?year={year}&team1goals={score}&team2goals={score}&page=1"
        res = requests.get(url)
        res_json = res.json()
        total = res_json["total"]
        count += total
    return count


if __name__ == "__main__":
    getNumDraws(2011)
