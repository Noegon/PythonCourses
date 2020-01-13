# task 2
iterations = [1, 2, 3, 5, 10, 20, 50, 100, 1000]
def sum_of_series(iterations: int) -> float:
    return sum(1.0 / 2 ** k for k in range(1, iterations + 1))

for i in iterations:
    print('Sum of series 1/2 + 1/4 + 1/8 + ... + 1/2^n for {0} iterations'.format(i))
    print(sum_of_series(iterations=i))