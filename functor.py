from types import FunctionType
from typing import Union

from pymonad import Functor, Just, List, curry


@curry
def add(x, y) -> Union[int, FunctionType, Functor]:
    return x + y


add10: Functor = add * Just(10)


if "__main__" == __name__:
    print(isinstance(add(1), Functor))  # True
    print(isinstance(add10, Functor))  # True
    print(add10 & Just(1))  # Just 11
    print(add10 & List(1, 2, 3, 4, 5))  # [11, 12, 13, 14, 15]
    print(add * Just(10) & List(1, 2, 3, 4, 5))  # [11, 12, 13, 14, 15]
