from pymonad import Just, Nothing, Maybe

# посадка птиц на левую сторону
to_left: Maybe = lambda num: lambda balance: (
    Nothing
    if abs((balance[0] + num) - balance[1]) > 4
    else Just((balance[0] + num, balance[1]))
)

# посадка птиц на правую сторону
to_right: Maybe = lambda num: lambda balance: (
    Nothing
    if abs((balance[1] + num) - balance[0]) > 4
    else Just((balance[0], balance[1] + num))
)

# банановая кожура
banana: Maybe = Nothing


# отображение результата
def show(maybe: Maybe) -> None:
    result = maybe.getValue() if maybe is not Nothing else 'Упал!'
    print(result)


# начальное состояние
begin: Maybe = Just((0, 0))


if '__main__' == __name__:

    show(begin >> to_left(2) >> to_right(5) >> to_left(-2))
    # "Упал!" - канатоходец упадёт тут

    show(begin >> to_left(2) >> to_right(5) >> to_left(-1))
    # (1, 5) - в данном случае всё ок

    show(begin >> to_left(2) >> banana >> to_right(5) >> to_left(-1))
    # "Упал!" кожура всё испортит
