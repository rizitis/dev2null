numbers = [4, 9, 14, 18, 24, 28, 34, 39, 44]

# Υπολογισμός των τριάδων
triplets = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            triplets.append([numbers[i], numbers[j], numbers[k]])

# Υπολογισμός των τετράδων
quads = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            for l in range(k+1, len(numbers)):
                quads.append([numbers[i], numbers[j], numbers[k], numbers[l]])

# Υπολογισμός των πεντάδων
quints = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            for l in range(k+1, len(numbers)):
                for m in range(l+1, len(numbers)):
                    quints.append([numbers[i], numbers[j], numbers[k], numbers[l], numbers[m]])

# Εγγραφή των τριάδων, τετράδων και πεντάδων σε αρχείο
with open('p4.txt', 'w') as f:
    f.write('Triplets:\n')
    for triplet in triplets:
        f.write(str(triplet) + '\n')
    f.write('Quads:\n')
    for quad in quads:
        f.write(str(quad) + '\n')
    f.write('Quints:\n')
    for quint in quints:
        f.write(str(quint) + '\n')

