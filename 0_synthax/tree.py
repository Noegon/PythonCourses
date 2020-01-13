# task 0
depth = 10

star_amounts = list(range(1, (depth * 2) + 1, 2))
for i in star_amounts:
    print(int(((star_amounts[-1] - i) / 2)) * ' ' + '*' * i)