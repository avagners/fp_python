from types import FunctionType
from typing import Union

from pymonad import curry


# 3.1.
@curry
def tag(tag: str, value: str) -> Union[str, FunctionType]:
    return f"<{tag}>{value}</{tag}>"


bold: FunctionType = tag("b")
italic: FunctionType = tag("i")


# 3.2.
@curry
def tag_attr(tag: str, attr: dict, value: str) -> Union[str, FunctionType]:
    params = ''.join(f' {key}="{value}"' for key, value in attr.items())
    return f"<{tag}{params}>{value}</{tag}>"


bold_attr: FunctionType = tag_attr("b")({'class': 'list-group', 'id': 'box'})


if "__main__" == __name__:
    print(bold("bold value"))
    print(italic("italic value"))
    print(bold_attr("bold with attr value"))
