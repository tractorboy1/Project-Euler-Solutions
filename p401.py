import math

def sum_of_squares_of_factors(n):
    total = 0
    if n == 1:
        total = 1
    else:
        for i in range(1, math.floor(n/2)+1):
            if n%i == 0:
                total += i**2
        total += n**2

    print(f"total for {n} is {total}")
    return total

def sum_of_k_squares(k):
    return ((k*(k+1)*(k*2+1))/6)

def diff(a, b):
    return (sum_of_k_squares(b)-sum_of_k_squares(a))

def sum_squares(s, e):
    return (e * (e + 1) * (e * 2 + 1) - s * (s + 1) * (s * 2 + 1)) // 6

def sigma2(n):
    total = 0
    #for i in range(1,math.floor(n**0.5)+1):
    #    total += i * diff(math.floor(n/(i+1)), math.floor(n/i))
    total += sum((i**2 * (n // i)) for i in range(1, math.floor(n**0.5)+1))
    total += sum((sum_squares(n // (i + 1), n // i) * i) for i in range(1, (n // (math.floor(n**0.5)+1)+1)))
    return total

def compute():
    LIMIT = 10**15
    MODULUS = 10**9

    # Can be any number from 1 to LIMIT, but somewhere near sqrt(LIMIT) is preferred
    splitcount = math.floor(LIMIT ** 0.5)
    # Consider divisors individually up and including this number
    splitat = LIMIT // (splitcount + 1)

    ans = sum((i * i * (LIMIT // i)) for i in range(1, splitat + 1))
    ans += sum((sum_squares(LIMIT // (i + 1), LIMIT // i) * i) for i in range(1, splitcount + 1))
    return str(ans % MODULUS)


if __name__ == "__main__":
	print(compute())