# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

numb = 0
count_ = 0
count_max = 0
numb_new = 0
for i in array:
    if count_max < count_:
        count_max = count_
        numb_new = numb
    count_ = 0
    for itm in array[1:]:
        if i == itm:
            numb = i
            count_ += 1

print(f'чаще всего встречается число {numb_new}')
