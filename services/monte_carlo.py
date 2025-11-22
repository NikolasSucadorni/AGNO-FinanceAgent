import numpy as np

class MonteCarlo:
    def simulate(self, initial, mean, volatility, steps=252, n=5000):
        dt = 1 / steps
        results = []
        for _ in range(n):
            prices = [initial]
            for _ in range(steps):
                shock = np.random.normal(mean * dt, volatility * np.sqrt(dt))
                prices.append(prices[-1] * (1 + shock))
            results.append(prices[-1])
        return np.array(results)
