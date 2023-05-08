with open('31-45.txt', 'r') as infile, open('morethan3.txt', 'w') as outfile:
    for line in infile:
        nums = line.strip().split()
        count = 0
        for num in nums:
            if 31 <= int(num) <= 45:
                count += 1
        if count == 3:
            outfile.write(line)

