import logging
from random import random
from typing import Dict, Tuple, List
from simulation.tournament import simulate_tournamet
from simulation.league import simulate_league


def start(option: int, teamlist: List[str]) -> Dict[str, float | int]:
    teams = {team: random() for team in teamlist}
    if option == 1:
        return simulate_league(teams, play_match)
    elif option == 2:
        return simulate_tournamet(teams, play_match)
    else:
        logging.error('Bad option.')
        raise KeyError


def win_probability(score1: int, score2: int) -> Tuple[float]:
    probability1 = score1 / \
        (score1 + score2 + (score1 + score2) / 3 * abs(score1 - score2) + 0.001)
    probability2 = score2 / \
        (score1 + score2 + (score1 + score2) / 3 * abs(score1 - score2) + 0.001)
    return probability1, probability2


def play_match(home_team: int, away_team: int, draws: bool) -> Tuple[int] | bool:
    random_digit = random()
    if not draws:
        return random_digit <= home_team / (home_team + away_team)
    p1, p2 = win_probability(home_team, away_team)
    if random_digit <= p1:
        home_team = 3
        away_team = 0
    elif p1 + p2 <= random_digit:
        home_team = 0
        away_team = 3
    else:
        home_team = 1
        away_team = 1
    return home_team, away_team
