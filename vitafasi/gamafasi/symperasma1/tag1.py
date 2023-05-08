with open("ppppresults.txt", "r") as input_file:
    with open("31-45.txt", "w") as output_file:
        for line in input_file:
            # Έλεγχος αν η γραμμή περιέχει αριθμούς από το 31 έως το 45
            if any(str(i) in line for i in range(31, 46)):
                output_file.write(line)

