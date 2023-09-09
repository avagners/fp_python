from functools import reduce
from typing import Callable, Tuple, List as list

from pymonad import List


# функия создания тренировочного полигона N x M
def create_square(n: int, m: int) -> set:
    square = set()
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            square.add((x, y))
    return square


# функция получения координат соседних областей
get_neighbors_by_point: Callable[[Tuple[int]], List] = lambda point: \
    List(
        point,
        (point[0] - 1, point[1]),
        (point[0] + 1, point[1]),
        (point[0], point[1] - 1),
        (point[0], point[1] + 1)
    )

# функция первого дня захвата
first_day: Callable[[list[int]], List] = lambda battalion: \
    List(*zip(battalion[::2], battalion[1::2]))

# функция каждого последующего дня захвата
next_day: Callable[[List], List] = lambda today: reduce(
    lambda x, y: x + y, map(get_neighbors_by_point, today)
)

# функция получения итоговых обласлей для захвата
valid: Callable[[int, int], List] = lambda n, m: lambda conquested_territory: \
    {conquested_territory}.intersection(create_square(n, m))


# функция вычисления дня полного захвата плацдарма
def full_conquest(n: int, m: int, conquested: List, day: int) -> int:
    if set(conquested) == create_square(n, m):
        return day
    next_day_conquest = List(conquested) >> next_day >> valid(n, m)
    return full_conquest(n, m, next_day_conquest, day + 1)


# итоговая функция
conquest_campaign: Callable[[int, int, list[int]], int] = lambda n, m, battalion: \
    full_conquest(n, m, first_day(battalion), 1)


if "__main__" == __name__:
    print(conquest_campaign(3, 4, [2, 2, 3, 4]))
    # 3
