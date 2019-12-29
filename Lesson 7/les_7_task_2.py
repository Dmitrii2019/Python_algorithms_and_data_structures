# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random

array = [random.uniform(0.0, 49.0) for _ in range(10)]
print(array)


def ms(array):
    n = len(array)
    if n < 2:
        return array
    l = ms(array[:n // 2])
    r = ms(array[n // 2:n])
    i = j = 0
    res = []
    while i < len(l) or j < len(r):
        if not i < len(l):
            res.append(r[j])
            j += 1
        elif not j < len(r):
            res.append(l[i])
            i += 1
        elif l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    return res


print(ms(array))

