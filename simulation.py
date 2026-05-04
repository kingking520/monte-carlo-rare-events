import numpy as np
import matplotlib.pyplot as plt
import os

def simulate_rare_event(simulations=1_000_000, mean=0.001, std=0.02, threshold=-0.05):
    np.random.seed(42)
    returns = np.random.normal(loc=mean, scale=std, size=simulations)
    rare_event = returns < threshold
    probability = np.mean(rare_event)
    return probability, returns

def plot_distribution(returns, threshold, output_path):
    plt.hist(returns, bins=100, density=True, alpha=0.6)
    plt.axvline(threshold, linestyle='--', label='Rare Event Threshold')
    plt.title("Monte Carlo Simulation of Returns")
    plt.legend()
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    prob, returns = simulate_rare_event()

    print(f"Estimated Probability of Extreme Loss: {prob}")

    base_dir = os.path.dirname(__file__)
    results_dir = os.path.join(base_dir, "..", "results")

    # Save output
    with open(os.path.join(results_dir, "output.txt"), "w") as f:
        f.write(f"Probability: {prob}")

    # Save plot
    plot_distribution(returns, -0.05, os.path.join(results_dir, "distribution.png"))