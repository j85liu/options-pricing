import numpy as np

def european_call_payoff(S_T, K):
    return np.maximum(S_T - K, 0)

def european_put_payoff(S_T, K):
    return np.maximum(K - S_T, 0)

# --- Industry Note ---
# Exotic payoffs often require custom logic: e.g., lookback, Asian (avg), barrier (with knock-in/out logic), etc.
