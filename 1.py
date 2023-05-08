import itertools

# Ορισμός των πιθανών αριθμών
numbers = list(range(1, 46))

# Δημιουργία όλων των πιθανών συνδυασμών 5 αριθμών
combinations = list(itertools.combinations(numbers, 5))

# Φιλτράρισμα των συνδυασμών που δεν πληρούν τις προϋποθέσεις
filtered_combinations = []
for combo in combinations:
    # Έλεγχος για 3 συνεχόμενους αριθμούς
    if (combo[0]+1 == combo[1] and combo[1]+1 == combo[2]) or (combo[1]+1 == combo[2] and combo[2]+1 == combo[3]) or (combo[2]+1 == combo[3] and combo[3]+1 == combo[4]):
        continue
    # Έλεγχος για περισσότερους από 2 αριθμούς από την ίδια δεκάδα
    if sum(1 for num in combo if num in range(1, 11)) > 2 or sum(1 for num in combo if num in range(11, 21)) > 2 or sum(1 for num in combo if num in range(21, 31)) > 2 or sum(1 for num in combo if num in range(31, 41)) > 2:
        continue
    filtered_combinations.append(combo)

# Ανοίγουμε το αρχείο εξόδου
with open("filtered_combinations.txt", "w") as outfile:
    # Εκτύπωση των φιλτραρισμένων πιθανών συνδυασμών στο αρχείο εξόδου
    for combo in filtered_combinations:
        outfile.write(' '.join(str(num) for num in combo) + '\n')

