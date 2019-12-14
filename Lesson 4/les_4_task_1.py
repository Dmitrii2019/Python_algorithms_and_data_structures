# 1)
import timeit
import cProfile
import random


def change_array(SIZE):
    MIN_ITEM = 10
    MAX_ITEM = 99
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    min_ = array[0]
    max_ = array[1]
    for i in array:
        for itm in array:
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
    return array, min_, max_


s = """ 
def change_array(SIZE):
    MIN_ITEM = 10
    MAX_ITEM = 15
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    min_ = array[0]
    max_ = array[1]
    for i in array:
        for itm in array:
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
    return array, min_, max_
    
change_array(400)
"""
# O(n2) – квадратичная сложность
# 0.154067428 change_array(100)
# 0.538166369 change_array(200)
# 2.19665313 change_array(400)
# print(timeit.timeit(s, number=100, globals=globals()))
cProfile.run('change_array(400)')


# 100
#   1    0.001    0.001    0.001    0.001 les_4_task_1.py:18(change_array)
# 100    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 130    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# 200
#   1    0.005    0.005    0.005    0.005 les_4_task_1.py:18(change_array)
# 200    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 274    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# 400
#   1    0.017    0.017    0.018    0.018 les_4_task_1.py:18(change_array)
# 400    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 559    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


def change_array2(SIZE):
    MIN_ITEM = 10
    MAX_ITEM = 99
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    min_ = min(array)
    max_ = max(array)
    min_ind = array.index(min_)
    max_ind = array.index(max_)
    array.insert(min_ind, max_)
    array.pop(min_ind + 1)
    array.insert(max_ind, min_)
    array.pop(max_ind + 1)
    return array, min_, max_


s2 = """ 
def change_array2(SIZE):
    MIN_ITEM = 10
    MAX_ITEM = 99
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    min_ = min(array)
    max_ = max(array)
    min_ind = array.index(min_)
    max_ind = array.index(max_)
    array.insert(min_ind, max_)
    array.pop(min_ind + 1)
    array.insert(max_ind, min_)
    array.pop(max_ind + 1)
    return array, min_, max_
    
change_array2(400)
"""


# O(n) – линейная сложность
# 0.021452957 change_array(100)
# 0.043491326 change_array(200)
# 0.09410325900000001 change_array(400)
# print(timeit.timeit(s2, number=100, globals=globals()))
# cProfile.run('change_array2(400)')
# 100
#   1    0.000    0.000    0.000    0.000 les_4_task_1.py:88(change_array2)
# 100    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 152    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# 200
#   1    0.000    0.000    0.001    0.001 les_4_task_1.py:88(change_array2)
# 200    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 283    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# 400
#   1    0.000    0.000    0.001    0.001 les_4_task_1.py:88(change_array2)
# 400    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 546    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

def change_array3(SIZE):
    MIN_ITEM = 10
    MAX_ITEM = 99
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

    idx_min = 0
    idx_max = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return array, array[idx_min], array[idx_max]


s3 = """
def change_array3(SIZE):
    MIN_ITEM = 10
    MAX_ITEM = 99
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

    idx_min = 0
    idx_max = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return array, array[idx_min], array[idx_max]
    
change_array3(400)
"""
# O(n) – линейная сложность
# 0.020423352 change_array(100)
# 0.040120482 change_array(200)
# 0.092640959 change_array(400)

print(timeit.timeit(s3, number=100, globals=globals()))
cProfile.run('change_array3(400)')

# 100
#   1    0.000    0.000    0.000    0.000 les_4_task_1.py:140(change_array3)
# 100    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 145    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# 200
#   1    0.000    0.000    0.001    0.001 les_4_task_1.py:140(change_array3)
# 200    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 275    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# 400
#   1    0.000    0.000    0.001    0.001 les_4_task_1.py:140(change_array3)
# 400    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 536    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# Взял эту задачку, так как по ней сделали замечание:
# "Вариант в строчках 19-24 не самый хороший с точки зрения асимптотики. Об этом поговорим на уроке вечером.
# А вот строка 11 приводит к фатальным ошибкам на тестовых данных"
# поправил код, что бы не было ошибки
# тест докозал что мой 1 вариан не сай лучший, самое большое время обработки кода и является
# O(n2) – квадратичная сложность, 2-й и 3-й (Ваш) вариант является O(n) – линейной сложности
# 3-й вариант лучше 2-го по читаемости и меньшему количеству операций, по замерам одинаковы.
