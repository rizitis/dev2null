with open("filtered_combinations.txt", "r") as input_file:
    with open("filtered_combinations_processed.txt", "w") as output_file:
        for line in input_file:
            nums = line.strip().split()
            groups = [int(num) // 10 for num in nums]
            if sum(groups.count(i) >= 3 for i in range(1, 6)) == 0:
                output_file.write(line)

