#print(f'{i} * {j} = {i * j}')


multipl = 1

for i in range(1,11):
    if i % 2 == 0:
        continue
    else:
        multipl *= i
print(multipl)