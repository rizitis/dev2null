# Ανοίγουμε ένα αρχείο για εγγραφή
output_file = open("katheta.txt", "w")

# Λίστα με όλους τους αριθμούς
numbers = [1, 6, 11, 16, 21, 26, 31, 36, 41]

# Υπολογισμός των τετράδων
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            for l in range(k+1, len(numbers)):
                tetrada = [numbers[i], numbers[j], numbers[k], numbers[l]]
                output_file.write(" ".join(str(x) for x in tetrada) + "\n")

# Κλείσιμο του αρχείου
output_file.close()

