# Trivially 1-9 are 1st power, and 1 digit
# 4-9 produce 2nd power which is 2 digits
# 5-9 produce 3rd powers which are 3 digits

total = 0
for n in range(1,10):
    for i in range(1,50):
        power = n**i
        if power >= 10**(i-1):
            total += 1
            print(f"The {i}th power of {n} is {power}")
        else:
            # If we didn't satisfy, no point in checking higher powers for this n
            continue
print(f"The total number is {total}")