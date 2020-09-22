def getWinnerTotalGoals(competition, year):
    import requests

    competition_base = "https://jsonmock.hackerrank.com/api/football_competitions"
    competition_url = f"{competition_base}?name={competition}&year={year}"
    competition_res = requests.get(competition_url)
    competition_res_json = competition_res.json()
    team = competition_res_json['data'][0]['winner']

    match_base = "https://jsonmock.hackerrank.com/api/football_matches"
    match_url1 = f"{match_base}?competition={competition}&year={year}&team1={team}"
    match_res1 = requests.get(match_url1)
    match_res1_json = match_res1.json()
    match_total_pages1 = match_res1_json['total_pages']

    match_url2 = f"{match_base}?competition={competition}&year={year}&team2={team}"
    match_res2 = requests.get(match_url2)
    match_res2_json = match_res2.json()
    match_total_pages2 = match_res2_json['total_pages']

    count = 0
    for i in range(1, match_total_pages1 + 1):
        match_url1 = f"{match_base}?competition={competition}&year={year}&team1={team}&page={i}"
        match_res1 = requests.get(match_url1)
        match_res1_json = match_res1.json()

        for match in match_res1_json['data']:
            count += int(match['team1goals'])

    for i in range(1, match_total_pages2 + 1):
        match_url2 = f"{match_base}?competition={competition}&year={year}&team2={team}&page={i}"
        match_res2 = requests.get(match_url2)
        match_res2_json = match_res2.json()

        for match in match_res2_json['data']:
            count += int(match['team2goals'])
    return count


if __name__ == "__main__":
    competition = "UEFA Champions League"
    year = 2011
    print(getWinnerTotalGoals(competition, year))
