from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

from shooting import zad1, zad2


if __name__ == "__main__":
    names = ('Symulator nr.1', 'Symulator nr.2')
    alpha = 0.05  # poziom istotności
    points = [task(100) for task in (zad1, zad2)]
    averages = (np.mean(points[0]), np.mean(points[1]))
    _, p_value = stats.ttest_ind(points[0], points[1]) # test studenta

    #testy
    if p_value < alpha:
        print('Odrzucamy hipotezę, ponieważ istnieją istotne różnice między wynikami symulatorów. Wartość p wynosi',p_value)
    else:
        print('Nie odrzucamy hipotezy. Nie ma istotnych różnic między wynikami symulatorów. Wartość p wynosi',p_value)
    print(f'Średnie wyniki\n{names[0]}\t{averages[0]}\n{names[1]}\t{averages[1]}')
    plt.bar(names, averages, width=0.3)
    plt.xlabel('Symulatory')
    plt.ylabel('Średnie')
    plt.show()
