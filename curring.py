from types import FunctionType
from typing import Union

from pymonad import curry


# 2.3.1
@curry
def _greeting1(greeting: str, name: str) -> Union[str, FunctionType]:
    return f"{greeting}, {name}!"


hello_name1: FunctionType = _greeting1("Hello")


# 2.3.2.
@curry
def _greeting2(greeting: str, sep: str, end: str, name: str) -> Union[str, FunctionType]:
    return f"{greeting}{sep} {name}{end}"


hello_name2: FunctionType = _greeting2("Hello")(",")("!")


if "__main__" == __name__:
    print(hello_name1("Tom"))
    print(hello_name2("Huckleberry"))
