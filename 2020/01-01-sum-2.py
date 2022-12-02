def sum_two(input, target_sum):
    sum_set = set()
    with open(input) as file:
        for line in file:
            num_a = int(line)
            num_b = target_sum - num_a
            if num_b in sum_set:
                return(num_a, num_b)
            sum_set.add(num_a)

a, b = sum_two("01-01-input.txt", 2020)
print((a, b), a * b)