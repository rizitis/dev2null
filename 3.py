import itertools

# Αρχικοί αριθμοί
numbers = [1, 10, 20, 30, 40]

# Συνδυασμοί από 1 έως 45 με πεντάδες που περιέχουν τουλάχιστον 3 αριθμούς από τους αρχικούς αριθμούς
combinations = itertools.combinations([i for i in range(1, 46)], 5)
valid_combinations = filter(lambda x: sum([1 for num in numbers if num in x]) >= 3, combinations)

# Εγγραφή των αποτελεσμάτων σε ένα αρχείο κειμένου
with open("tetrada.txt", "w") as f:
    for comb in valid_combinations:
        f.write(str(comb) + "\n")

