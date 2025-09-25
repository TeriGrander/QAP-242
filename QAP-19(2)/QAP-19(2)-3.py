def generate_combinations(colors, sizes):
   for color in colors:
       for size in sizes:
           yield color, size

combination_generator = generate_combinations(["red", "blue", "green"], ["small", "large"])
for combination in combination_generator:
   print(combination)