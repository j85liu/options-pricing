# 🧠 Institutional Option Pricing — A Simplified Monte Carlo Framework

This project walks through a simplified but realistic pipeline for pricing options using **Monte Carlo simulation**, inspired by how professionals like [Dr. Amal Moussa](https://www.goldmansachs.com/our-firm/people/leadership/amal-moussa.html)—Head of Exotic Derivatives at Goldman Sachs—approach pricing at the institutional level.

The goal is **educational**: understand how options are priced in practice, with code that's simple enough to learn from, but includes comments showing how it's done at scale in industry.

---

## 📊 Features

### ✅ Implemented Models
| Model Type        | Name                  | Notes |
|-------------------|-----------------------|-------|
| Analytical        | Black-Scholes         | Benchmark, closed-form |
| Simulation-Based  | Monte Carlo (GBM)     | Simple stochastic process |
| Simulation-Based  | Monte Carlo (Heston)  | Includes stochastic volatility (smile/skew) |

### 🧾 Payoffs
- European Call (✓)
- European Put (✓)
- *Comments included on how to extend to Asian, Barrier, and Lookback options*

---

## 🧪 What's Inside

### `notebooks/01_monte_carlo_option_pricing.ipynb`
A complete walkthrough:
- Generates GBM paths
- Calculates expected payoff
- Discounts back to present value
- Compares to Black-Scholes
- Comments on variance reduction & production usage

### `models/`
Modular Python files:
- `monte_carlo.py`: GBM and Heston path generation
- `payoff.py`: Payoff logic for European options
- `black_scholes.py`: Closed-form BSM calculator

---

## 🔍 Industry Comments (🧠 Learn More)

This repo includes **inline comments** explaining:
- Why traders use Monte Carlo for complex derivatives
- How real-world pricing involves stochastic vol (Heston, SABR, local vol)
- What differentiates retail vs institutional models
- How model choice is tied to market regime, product complexity, and calibration quality

---
