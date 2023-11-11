from typing import List
from scipy import stats
import numpy as np
from simulation import start


def main():
    '''
    option = int(input())
    simulation_number = int(input())
    teams: List[str] = []
    while True:
        team = input()
        if team == '':
            break
        teams.append(team)
    '''
    teams: List[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    simulation_number = 31
    option = 1
    alpha = 0.05
    expected_value = 3 * len(teams) - 3
    # ret = new_simulation(teams, option, simulation_number)
    # z_score = (np.mean(ret) - expected_value) / \
    #     (np.std(ret) / np.sqrt(len(ret)-1)) # Z = (śr. - oczekiwana wartość/ odch. stand.)
    # p_value_z = stats.norm.sf(abs(z_score)) * 2

    # print('Z test value:', z_score)
    # if p_value_z < alpha:
    #     print(
    #         f"Reject the hypothesis that the average result is equal 3n-3 for alpha={alpha}. Value is {p_value_z}")
    # else:
    #     print(
    #         f"Do not reject the hypothesis that the average result is equal 3n-3 for alpha={alpha}. Value is {p_value_z}")

    league = new_simulation(teams, 2, 100)
    correlation, _ = stats.pearsonr(league, range(len(league)))
    print('Pearsons correlation for tournament average:', correlation)


def new_simulation(teams, option, simulation_number):
    ret = []
    for _ in range(simulation_number):
        results = start(option, teams)
        ret.extend([results[r] for r in results])
    return ret


if __name__ == "__main__":
    main()
