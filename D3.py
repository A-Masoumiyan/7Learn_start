# filter map zip
from data.data import teams


# lambda team, name: team['score'] * 2


def pars_result(team):
    return {
        'name': team['name'],
        'win': team['result'].count('w'),
        'lose': team['result'].count('l'),
        'draw': team['result'].count('d'),
    }


def calculate_score(team):
    score = (team['win'] * 3) + team['draw']
    team['score'] = score
    return team


tmp_score_board = list(map(pars_result, teams))

score_board = map(calculate_score, tmp_score_board)


def check_score(team):
    return team['score'] >= 30


# passed_teams = filter(check_score, score_board)
passed_teams = list(filter(lambda t: t['score'] >= 30, score_board))

for team in passed_teams:
    print(team)
