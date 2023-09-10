from functools import reduce
from typing import Callable, List


# Функция сравнения текущего числа с числами из кортежа максимальных чисел
# В итоге мы получаем актуальный кортеж двух максимальных чисел
def two_max_numb(two_max_numbers: tuple, current: int) -> tuple:
    first_max, second_max = two_max_numbers
    if current > first_max:
        return current, first_max
    if current > second_max:
        return first_max, current
    return first_max, second_max


# Функция нахождения второго максимального числа в массиве
get_second_max: Callable[[List[int]], int] = lambda numbers: reduce(
    two_max_numb, numbers, (-float('inf'), -float('inf'))
)[1]


if "__main__" == __name__:
    print(get_second_max([5, 4, 3, 2, 5]))  # 5
    print(get_second_max([5, 4, 3, 2]))  # 4
    print(get_second_max([0, 0, 1, 2]))  # 1
    print(get_second_max([-1, -2, -3, -2]))  # -2
    print(get_second_max([-1, -1, -3, -2]))  # -1
