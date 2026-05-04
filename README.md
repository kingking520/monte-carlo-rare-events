# Monte Carlo Rare Event Simulation

## Overview
This project estimates the probability of extreme financial losses using Monte Carlo simulation.

## Method
- Simulated 1,000,000 random outcomes
- Assumed normal distribution of returns
- Calculated probability of losses below -5%

## Output
- Probability result saved in results/output.txt
- Distribution plot saved in results/distribution.png

## How to Run
pip install -r requirements.txt
python src/simulation.py