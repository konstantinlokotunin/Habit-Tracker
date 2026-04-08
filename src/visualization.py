import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")

def plot_habits(dates, habits):
    _, ax = plt.subplots(figsize=(10, 5))

    x = np.arange(len(dates))  # numeric positions
    width = 0.25              # bar width

    colors = ["#4C72B0", "#55A868", "#C44E52"]

    for (habit, values), color in zip(habits.items(), colors):
        ax.plot(x, values, marker='o', label=habit, color=color)

    # Center x-axis labels
    ax.set_xticks(x)
    ax.set_xticklabels(dates, rotation=45)

    ax.set_title("Habit Completion Over Time")
    ax.set_ylabel("Completed (1/0)")
    ax.set_xlabel("Date")

    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()

