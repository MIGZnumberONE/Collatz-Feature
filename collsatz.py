import matplotlib.pyplot as plt

def collatz_analysis_with_plot(n):
    steps = 0
    divide_by_2_count = 0
    multiply_3_plus_1_count = 0
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
            divide_by_2_count += 1
        else:
            n = 3 * n + 1
            multiply_3_plus_1_count += 1
        sequence.append(n)
        steps += 1

    # Output Folge
    print("\nCollatz-Folge:")
    for num in sequence:
        print(num)

    # Statistiken
    print("\nAnfangszahl:", sequence[0])
    print("Anzahl Schritte:", steps)
    print("Teilungen durch 2:", divide_by_2_count)
    print("×3 + 1 Schritte:", multiply_3_plus_1_count)

    # Graph
    plt.figure(figsize=(10, 5))
    plt.plot(sequence, marker='o', linestyle='-', color='blue')
    plt.title(f'Collatz-Folge für Startwert {sequence[0]}')
    plt.xlabel('Schritt')
    plt.ylabel('Zahlenwert')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Input USER
zahl = int(input("Gib Zahl ein: "))
collatz_analysis_with_plot(zahl)