import numpy as np

def generate_gbm_paths(S0, r, sigma, T, steps, n_paths):
    dt = T / steps
    paths = np.zeros((steps + 1, n_paths))
    paths[0] = S0

    for t in range(1, steps + 1):
        z = np.random.standard_normal(n_paths)
        paths[t] = paths[t - 1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)

    return paths

# --- Industry Note ---
# In production, models simulate under the risk-neutral measure.
# Firms also use antithetic variates, control variates, or low-discrepancy sequences (Sobol) to reduce variance.

def generate_heston_paths(S0, T, r, v0, kappa, theta, sigma_v, rho, steps, n_paths):
    dt = T / steps
    prices = np.zeros((steps + 1, n_paths))
    variances = np.zeros((steps + 1, n_paths))
    prices[0] = S0
    variances[0] = v0

    for t in range(1, steps + 1):
        z1 = np.random.standard_normal(n_paths)
        z2 = rho * z1 + np.sqrt(1 - rho ** 2) * np.random.standard_normal(n_paths)
        
        variances[t] = np.maximum(
            variances[t - 1] + kappa * (theta - variances[t - 1]) * dt +
            sigma_v * np.sqrt(variances[t - 1] * dt) * z2, 0
        )
        prices[t] = prices[t - 1] * np.exp((r - 0.5 * variances[t - 1]) * dt + np.sqrt(variances[t - 1] * dt) * z1)

    return prices
