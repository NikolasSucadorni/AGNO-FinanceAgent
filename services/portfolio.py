import numpy as np

class PortfolioService:
    def simulate_portfolio(self, assets, weights):
        returns = np.array([a['return'] for a in assets])
        w = np.array(weights)
        portfolio_return = np.sum(returns * w)
        return portfolio_return
