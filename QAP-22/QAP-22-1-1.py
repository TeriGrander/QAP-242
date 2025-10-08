import random
import time

# Генерация списка случайных чисел
arr = [random.randint(0, 10000) for _ in range(1000)]

def find_duplicates_1(arr):
    duplicates = []
    for i in range(len(arr)-1):
        if arr[i] in arr[i+1:]: duplicates.append(arr[i])

def find_duplicates_2(arr):
  duplicates = []
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] == arr[j]:
        duplicates.append(arr[i])
  return duplicates

start_time = time.time()
find_duplicates_1(arr)
print("your try took {:.5f} seconds".format(time.time() - start_time))

start_time = time.time()
find_duplicates_2(arr)
print("original algorithm took {:.5f} seconds".format(time.time() - start_time))