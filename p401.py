import math

def sum_squares(s, e):
    return (e * (e + 1) * (e * 2 + 1) - s * (s + 1) * (s * 2 + 1)) // 6

def part1(n):
    # For integers below sqrt n, they will appear floor(n//i) times
    sum = 0
    sqrt = math.floor(n**0.5)
    limit = n // (sqrt+1)
    for i in range(1, limit+1):
        sum += i**2 * (n//i)
    return sum

def part2(n):
    # How to sum consecutive square numbers is known.
    # When k is large, m = floor(n/k) does not change, in particular
    # when k is (n//2)+1 to n, the floor is always 1
    # So from (n//2)+1, each number appears only once, and so the total is just
    # (sumofsquares(n) - sumofsquares(n//2))
    sum = 0
    sqrt = math.floor(n**0.5)
    for i in range(1, sqrt+1):
        sum += sum_squares(n//(i+1), (n // i)) * i

    return sum

def total(n):
    return (part1(n) + part2(n))

print(total(10**15) % 10**9)