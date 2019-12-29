# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = array[0]
max_ = 0
for i in array:
    for itm in array[1:]:
        if max_ < itm > i:
            max_ = itm
        elif min_ > itm < i:
            min_ = itm

min_ind = array.index(min_)
max_ind = array.index(max_)
array.insert(min_ind, max_)
array.pop(min_ind + 1)
array.insert(max_ind, min_)
array.pop(max_ind + 1)

print(array)
print(min_, max_)
