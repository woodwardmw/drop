from os import stat
import random
import statistics
import numpy as np
from matplotlib import pyplot as plt

class Attempt:
    def __init__(self) -> None:
        self.prob = 0.6
        self.tosses = 0
        self.success = False
    
    def toss(self) -> None:
        self.tosses += 1
        if random.random() < self.prob:
            self.prob += 0.01
            if self.prob < 1:
                self.toss()
            else:
                self.success = True

                return
        else:
            return

class Run:
    def __init__(self) -> None:
        self.tosses = 0
        self.success = False
    
    def run(self) -> int:
        while not self.success:
            attempt = Attempt()
            attempt.toss()
            self.tosses += attempt.tosses

            if attempt.success:
                self.success = True
        return self.tosses

def main():
    num_runs = 1000
    results = []
    for _ in range(num_runs):
        run = Run()
        results.append(run.run())
    print(f'Mean: {statistics.mean(results)}\nMax: {max(results)}\nS.D.: {statistics.stdev(results)}')

    bins = np.arange(0, max(results), 10000)
    plt.xlim([min(results), max(results)])
    plt.hist(results, bins=bins, alpha=0.5)
    plt.title(f'Number of attempts before success, {num_runs:,} runs. (Mean: {statistics.mean(results):,.0f})')
    plt.xlabel('Number of attempts before success')
    plt.ylabel('count')
    plt.savefig('histogram.png')

if __name__ == "__main__":
    main()
