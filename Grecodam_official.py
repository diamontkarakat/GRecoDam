import random
import numpy as np
from datetime import datetime

class HarmonySearch:
    def __init__(self, data_file, qirr, v_initial, A, B, L, n, vmin, vmax):
        self.Qin = np.loadtxt(data_file, dtype=float)
        self.qirr = qirr
        self.v_initial = v_initial
        self.A = A
        self.B = B
        self.L = L
        self.dh_initial = 3 * v_initial / (L * (A + B))
        self.Vin = np.cumsum(self.Qin) + v_initial - qirr
        self.n = n
        self.vmin = vmin
        self.vmax = vmax
        self.time = [x for x in range(1, 365)]
        self.seed = datetime.now()

    def objective_function(self, x1):
        Vcur = self.Vin - x1
        dh = np.array((3 * Vcur) / (self.L * (self.A + self.B)))
        E = (1000 * 9.81 * self.n * (x1 / 86400) * dh) / 1000000
        return sum(E)

    def initialize_harmony_memory(self, hms):
        hm = np.array([np.array([random.randint(1, 500000) for _ in range(364)]) for _ in range(hms)])
        row = [self.objective_function(hm[:, i]) for i in range(hms)]
        hm = np.vstack([hm, row])
        return hm

    def sort_harmony_memory(self, hm):
        return hm[:, hm[-1, :].argsort()]

    def harmony_search_algorithm(self, hms, hmcr, par, iterations):
        hm = self.initialize_harmony_memory(hms)
        hmsort = self.sort_harmony_memory(hm)

        for k in range(iterations):
            new_harmony = np.array([])

            if random.random() < hmcr:
                for i in range(364):
                    a = random.randint(0, hms - 1)
                    new_harmony = np.append(new_harmony, hmsort[i, a])

                if random.random() < par:
                    new_harmony = new_harmony + np.random.uniform(-500000.0, 500000.0, 364)
            else:
                new_harmony = np.array([random.randint(1, 500000) for _ in range(364)])

            new_harmony_eval = self.objective_function(new_harmony)
            if new_harmony_eval > hmsort[364, 0]:
                hmsort[:, 0] = np.append(new_harmony, new_harmony_eval)

            hmsort = self.sort_harmony_memory(hmsort)
            print(k)

        return hmsort

        def plot_hmsort_vs_time(self, hmsort):
            plt.plot(self.time, hmsort[:-1, 0], label='Best Harmony')
            plt.xlabel('Time')
            plt.ylabel('Objective Function Value')
            plt.title('Harmony Search Results')
            plt.legend()
            plt.imshow(img.reshape((28, 28)))
            plt.show()
            plt.savefig

# Example usage:
hs = HarmonySearch("data2.csv", 86400, 1000000, 50, 100, 1000, 0.75, 200000, 1500000)
result = hs.harmony_search_algorithm(hms=3, hmcr=0.7, par=0.5, iterations=1000)

# Plot the results
hs.plot_hmsort_vs_time(result)
