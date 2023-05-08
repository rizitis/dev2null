diagonios_file = open("katheta4.txt", "r")
temp9_file = open("result3.txt", "r")
output_file = open("result4.txt", "w")

# Δημιουργία dictionary με τις γραμμές του αρχείου diagonios
diagonios = {}
for line in diagonios_file:
    line = line.strip()
    diagonios[line] = True

# Έλεγχος για ταυτοσημείες στο αρχείο temp9.txt και εγγραφή στο αρχείο εξόδου
for line in temp9_file:
    line = line.strip()
    if line not in diagonios:
        output_file.write(line + "\n")

diagonios_file.close()
temp9_file.close()
output_file.close()

