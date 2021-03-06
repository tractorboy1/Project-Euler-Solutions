def sum_of_nat_numbers_below(n):
    total = sum(x for x in range(n) if (x%3 == 0 or x%5 == 0))

    return total

print(sum_of_nat_numbers_below(1000))