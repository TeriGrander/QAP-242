class AreaPoint:
    def __init__(self, i, j, height = 15):
       self.i = i
       self.j = j
       self.height = height

area_list = []
for i in range(3):
    line = []
    for j in range(3):
        line.append(AreaPoint(j, i))
    area_list.append(line)

print(area_list)