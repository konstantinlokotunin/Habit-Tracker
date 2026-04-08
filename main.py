from src.data_loader import load_data
from src.analysis import calculate_completion_rate, calculate_streak
from src.visualization import plot_habit_heatmap


def main():
    dates, habits = load_data("data/data.csv")

    for habit, values in habits.items():
        rate = calculate_completion_rate(values)
        streak = calculate_streak(values)

        print(f"{habit.capitalize()}:")
        print(f"  Completion Rate: {rate:.2f}%")
        print(f"  Max Streak: {streak}\n")

    plot_habit_heatmap(dates, habits)


if __name__ == "__main__":
    main()
