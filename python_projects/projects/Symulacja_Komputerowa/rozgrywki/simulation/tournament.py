import numpy as np
from typing import Callable, Dict


def simulate_tournamet(teams: Dict[str, float], play_match: Callable):
    for _ in range(int(np.log2(len(teams)))):
        teams_copy = [teams[num] for num in teams]
        keyset = [key for key in teams]
        # print(f'1/{int(len(teams)/2)}\nTeams left: {", ".join(sorted(keyset))}')
        for i in range(0, len(teams_copy), 2):
            if play_match(teams_copy[i], teams_copy[i+1], False) is True:
                del teams[keyset[i+1]]
            else:
                del teams[keyset[i]]
    return teams