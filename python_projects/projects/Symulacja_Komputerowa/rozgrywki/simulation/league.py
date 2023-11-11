from typing import Callable, Tuple, Dict


def simulate_league(teams: Dict[str, float], play_match: Callable[[int, int], Tuple[int]]) -> Dict[str, int]:
    results: Dict[str, int] = {key: 0 for key in teams}

    for home_team in teams:
        for away_team in teams:
            if home_team != away_team:
                # Each team plays against each other twice, once at home, once away
                score = play_match(teams[home_team], teams[away_team], True)
                results[home_team] += score[0]
                results[away_team] += score[1]
    return results
