# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
import timeit
import cProfile


def func_not_sieve(num_ind):
    sieve = []
    prime_numbers = []
    max_number = 2
    while len(prime_numbers) != num_ind:
        max_number += 1
        sieve = [i for i in range(max_number)]
        sieve[1] = 0
        for i in range(2, max_number):
            if sieve[i] != 0:
                for itm in range(i + i, len(sieve), i):
                    if sieve[itm] % i == 0:
                        sieve[itm] = 0
        prime_numbers = [i for i in sieve if i != 0]
    return prime_numbers[num_ind - 1]


print(func_not_sieve(3))  # для проверки функции

s = """
def func_not_sieve(num_ind):
    sieve = []
    prime_numbers = []
    max_number = 2
    while len(prime_numbers) != num_ind:
        max_number += 1
        sieve = [i for i in range(max_number)]
        sieve[1] = 0
        for i in range(2, max_number):
            if sieve[i] != 0:
                for itm in range(i + i, len(sieve), i):
                    if sieve[itm] % i == 0:
                        sieve[itm] = 0
        prime_numbers = [i for i in sieve if i != 0]
    return prime_numbers[num_ind - 1]

func_not_sieve(40)
"""

# 0.007228986  func_not_sieve(5)
# 0.031826586000000004 func_not_sieve(10)
# 0.140745387 func_not_sieve(20)
# 0.842036661   func_not_sieve(40)
# O(n2) – квадратичная сложность

print(timeit.timeit(s, number=100, globals=globals()))
cProfile.run('func_not_sieve(40)')

# 10
#   1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 200    0.000    0.000    0.000    0.000 {built-in method builtins.len}

# 20
#   1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#   1    0.001    0.001    0.001    0.001 df2.py:8(func_not_sieve)
# 872    0.000    0.000    0.000    0.000 {built-in method builtins.len}

# 40
#  1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#  1    0.008    0.008    0.010    0.010 df2.py:8(func_not_sieve)
#  1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
# 4046   0.000    0.000    0.000    0.000 {built-in method builtins.len}


def func_sieve(num_ind):
    sieve = []
    prime_numbers = []
    max_number = 2
    while len(prime_numbers) != num_ind:
        max_number += 1
        sieve = [i for i in range(max_number)]
        sieve[1] = 0
        for i in range(2, max_number):
            if sieve[i] != 0:
                j = i + i
                while j < max_number:
                    sieve[j] = 0
                    j += i
        prime_numbers = [i for i in sieve if i != 0]
    return prime_numbers[num_ind - 1]


print(func_sieve(3))  # для проверки функции

s1 = """
def func_sieve(num_ind):
    sieve = []
    prime_numbers = []
    max_number = 2
    while len(prime_numbers) != num_ind:
        max_number += 1
        sieve = [i for i in range(max_number)]
        sieve[1] = 0
        for i in range(2, max_number):
            if sieve[i] != 0:
                j = i + i
                while j < max_number:
                    sieve[j] = 0
                    j += i
        prime_numbers = [i for i in sieve if i != 0]
    return prime_numbers[num_ind - 1]


func_sieve(40)
"""
# 0.00425389     func_not_sieve(5)
# 0.017775859    func_not_sieve(10)
# 0.1009291069   func_not_sieve(20)
# 0.565371643   func_not_sieve(40)
# O(n2) – квадратичная сложность

print(timeit.timeit(s1, number=100, globals=globals()))
cProfile.run('func_sieve(40)')

# 10
#  1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 29    0.000    0.000    0.000    0.000 {built-in method builtins.len}

# 20
#  1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#  1    0.001    0.001    0.001    0.001 df2.py:69(func_sieve)
#  1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 71    0.000    0.000    0.000    0.000 {built-in method builtins.len}

# 40
#  1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#  1    0.004    0.004    0.005    0.005 df2.py:69(func_sieve)
#  1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
# 173   0.000    0.000    0.000    0.000 {built-in method builtins.len}

# Сложность у двух функций одинакова O(n2) – квадратичная сложность
# func_sieve - по скорости быстрее
