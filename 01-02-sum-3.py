def sum_three(input, target_sum):
    with open(input) as file:
        num_list = [int(num_a.strip()) for num_a in file]

        for num_a in num_list:
            for num_b in num_list:
                num_c = target_sum - num_a - num_b
                if num_c in num_list:
                    return(num_a, num_b, num_c)

a, b, c = sum_three("01-01-input.txt", 2020)
print((a, b, c), a * b * c)
