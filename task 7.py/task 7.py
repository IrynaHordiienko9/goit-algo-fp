import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    counts = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        counts[total] += 1
    probabilities = {dice_sum: counts[dice_sum] / num_rolls for dice_sum in counts}
    return probabilities


def theoretical_probabilities():
    probabilities = {
        2: 0.0278,
        3: 0.0556,
        4: 0.0833,
        5: 0.1111,
        6: 0.1389,
        7: 0.1667,
        8: 0.1389,
        9: 0.1111,
        10: 0.0833,
        11: 0.0556,
        12: 0.0278
    }
    return probabilities


def build_comparison_chart(empirical, theoretical):
    sums = list(empirical.keys())
    empirical_values = [empirical[s] for s in sums]
    theoretical_values = [theoretical[s] for s in sums]

    print("\nПopiвняння емпіричних та теоретичних ймовірностей:")
    print("Сума | Емпірична | Теоретична")
    print("-" * 32)
    for s, e, t in zip(sums, empirical_values, theoretical_values):
        print(f"{s:>4} | {e:.6f} | {t:.6f}")

    plt.figure(figsize=(10, 6))
    bar_width = 0.35
    x_positions = range(len(sums))

    bars_empirical = plt.bar([x - bar_width/2 for x in x_positions], empirical_values, width=bar_width, label='Емпірична', color='#4CAF50')
    bars_theoretical = plt.bar([x + bar_width/2 for x in x_positions], theoretical_values, width=bar_width, label='Теоретична', color='#2196F3')

    plt.xticks(x_positions, sums)
    plt.xlabel('Сума чисел')
    plt.ylabel('Ймовірність')
    plt.title('Порівняння емпіричних та теоретичних ймовірностей')
    plt.legend()
    plt.tight_layout()

    for bar in bars_empirical:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.002, f"{bar.get_height()*100:.2f}%", ha='center', va='bottom', fontsize=8, color='black')
    for bar in bars_theoretical:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 0.005, f"{bar.get_height()*100:.2f}%", ha='center', va='top', fontsize=8, color='white')

    plt.savefig('dice_probabilities_comparison.png')
    print("\nГpафiк збережено y файл: dice_probabilities_comparison.png")
    plt.show()


if __name__ == "__main__":
    num_trials = 1_000_000
    empirical_probs = simulate_dice_rolls(num_trials)
    theoretical_probs = theoretical_probabilities()
    build_comparison_chart(empirical_probs, theoretical_probs)
