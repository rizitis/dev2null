# Άνοιγμα του αρχείου morethan3.txt και ανάγνωση του περιεχομένου του
with open("morethan3.txt", "r") as f:
    lines = f.readlines()

# Αφαίρεση των γραμμών που περιέχουν αριθμούς από το 11-30
new_lines = [line for line in lines if not any(int(num) in range(11, 31) for num in line.split())]

# Άνοιγμα ενός νέου αρχείου για εγγραφή
with open("teliko.txt", "w") as f:
    # Γράψιμο των γραμμών που δεν περιέχουν αριθμούς από το 11-30
    f.writelines(new_lines)

