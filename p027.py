import math


class Quadratic():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.product = a*b

    def sum_for_n(self, n):
        return (n**2 + self.a * n + self.b)

    def check_for_consecutive_primes(self):
        for n in range(100):
            if not self.is_prime(self.sum_for_n(n)):
                return n

        return n

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n / i == n // i:
                return False

        return True

def main():
    current_max_run = 0
    product = 0
    for a in range(-1000,1001):
        for b in range(-1000,1001):
            quad = Quadratic(a,b)
            n = quad.check_for_consecutive_primes()
            if n > current_max_run:
                current_max_run = n
                product = quad.product
                max_a = a
                max_b = b
    print(f"Max run was {current_max_run} for a={max_a}, b={max_b}, i.e. product {product}")
    return product

if __name__ == "__main__":
    # execute only if run as a script
    main()