
class NumberToTheNumber():
    def __init__(self, number):
        self.value = number ** number

total = 0
for n in range(1000):
    if n % 10 == 0:
        pass
    else:
        item = NumberToTheNumber(n)
        total += item.value
print(total % 10 ** 10)