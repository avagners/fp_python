from functools import reduce
from typing import Callable, List


# функция расчета дельты времени
delta_time: Callable[[List[int]], List[int]] = lambda time: [time[0]] + list(
    map(lambda x, y: x - y, time[1:], time[:-1])
)

# функция получения массивов времени и скорости
get_time_and_speed: Callable[[List[int]], List[int]] = lambda massive: (
    delta_time(massive[1::2]), massive[0::2]
)

# итоговая функция расчета пути
odometr: Callable[[List[int]], int] = lambda massive: reduce(
    lambda path1, path2: path1 + path2,
    map(lambda time, speed: time * speed, *get_time_and_speed(massive))
)


if "__main__" == __name__:
    print(odometr([15, 1, 25, 2, 30, 3, 10, 5]))  # 90
    print(odometr([10, 1, 20, 2]))  # 30
