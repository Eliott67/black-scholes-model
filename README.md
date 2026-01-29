# black-scholes-model
Derivation and implementation of the Black-Scholes model using Stochastic Calculus and PDEs.

# Black-Scholes Model: Probabilistic & PDE Approach

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Overview

This project explores the mathematical foundations of the **Black-Scholes option pricing model**, establishing the duality between two major approaches in quantitative finance:
1.  **Stochastic Calculus:** Using Martingales, Itô's Lemma, and Girsanov's Theorem to define the risk-neutral measure.
2.  **Partial Differential Equations (PDEs):** Deriving the pricing equation via dynamic hedging and replication arguments.

The repository includes a comprehensive theoretical report and a Python implementation for numerical simulations.

## Key Features

* **Theoretical Proofs:** Rigorous derivation of the Black-Scholes PDE and the risk-neutral valuation formula.
* **Monte-Carlo Simulation:** Generation of Geometric Brownian Motion (GBM) paths to visualize asset dynamics.
* **Convergence Analysis:** Numerical verification of the Law of Large Numbers applied to option pricing.
* **The Greeks:** Sensitivity analysis (Delta, Gamma, Theta, Vega, Rho) implemented from scratch.

## Visualizations

### Brownian Motion Simulation
*(Place here a screenshot of your Brownian Motion paths from the report)*

## Project Structure

```bash
├── report/
│   └── Black_Scholes_Report.pdf  # Full mathematical report (LaTeX)
├── src/
│   ├── simulation.py             # Geometric Brownian Motion paths
│   ├── pricing.py                # Closed-form and Monte-Carlo pricers
│   └── greeks.py                 # Sensitivity analysis
├── requirements.txt
└── README.md
