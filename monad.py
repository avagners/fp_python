from pymonad import Just, Nothing, Maybe

# посадка птиц на левую сторону
to_left: Maybe = lambda num: lambda balace: (
    Nothing
    if abs((balace[0] + num) - balace[1]) > 4
    else Just((balace[0] + num, balace[1]))
)

# посадка птиц на правую сторону
to_right: Maybe = lambda num: lambda balace: (
    Nothing
    if abs((balace[1] + num) - balace[0]) > 4
    else Just((balace[0], balace[1] + num))
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

    show(begin
         >> to_left(2)
         >> to_right(5)
         >> to_left(-2))  # "Упал!" - канатоходец упадёт тут

    show(begin
         >> to_left(2)
         >> to_right(5)
         >> to_left(-1))  # (1, 5) - в данном случае всё ок

    show(begin
         >> to_left(2)
         >> banana  # "Упал!" кожура всё испортит
         >> to_right(5)
         >> to_left(-1))
