class IntDataFrame:
    def __init__(self, lst) -> None:
        self.column = []
        for i in lst: self.column.append(int(i))
    
    def count(self):
        number = 0
        for i in self.column:
            if i != 0: number += 1
        return number
    
    def unique(self):
        return len(set(self.column))


df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

print(df.column)
# [4, 4, 3, 0, 2, 0, 4]

print(df.count())
# 5

print(df.unique())
# 4