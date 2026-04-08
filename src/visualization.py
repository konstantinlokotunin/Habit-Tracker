import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

plt.style.use("seaborn-v0_8")

def plot_habit_heatmap(dates, habits):
    habit_names = list(habits.keys())
    
    # Convert dict → matrix
    data = np.array([habits[h] for h in habit_names])

    fig, ax = plt.subplots(figsize=(12, 2.5))

    cax = ax.imshow(data, aspect='auto', cmap = ListedColormap(["#e9ecef", "#3b82f6"]), vmin=0, vmax=1)

    # Labels
    ax.set_yticks(np.arange(len(habit_names)))
    ax.set_yticklabels((h.title() for h in habit_names), fontsize=12, fontweight='normal')

    ax.set_xticks(np.arange(len(dates)))
    ax.set_xticklabels(dates, fontsize=10, fontweight='normal', rotation=30)
   
    
    ax.grid(color="white", linestyle='-', linewidth=0.001)

    ax.set_title("Habit Completion (Weekly Overview)", fontsize=16, fontweight='light', pad=12)

    # Color bar (legend)
    cbar = fig.colorbar(cax)
    cbar.set_ticks([0, 1])
    cbar.set_ticklabels(["Missed", "Completed"])

    plt.tight_layout()
    plt.show()


