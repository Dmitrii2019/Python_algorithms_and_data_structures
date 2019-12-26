# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array1 = [i for i in array if i < 0]

max_namber = array1[0]

for i in array1:
    for itm in array1[1:]:
        if max_namber < i > itm:
            max_namber = i

print(f'максимальый отрицательный элемент {max_namber}, позиция в массиве {array.index(max_namber)}')
