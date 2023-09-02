from types import FunctionType

from pymonad import State, curry, unit


@curry
def buy(product: tuple, user: dict) -> State:
    product_name: str = product[0]
    product_amount: int = product[1]
    user_balance: int = user["money"]
    user_items: list = user["items"]

    @State
    def state(сheck_total: int) -> tuple:
        if product_name not in items.keys():
            print(f"Товара '{product_name}' нет в магазине.\n")
            return (user, сheck_total)
        product_price: int = items.get(product_name)
        cost: int = product_price * product_amount
        if cost > user_balance:
            print(f"Для покупки '{product_name}' в кол-ве {product_amount} шт."
                  " недостаточно средств.\n")
            return (user, сheck_total)
        user_state: dict = {"items": user_items + [product],
                            "money": user_balance - cost}
        return (user_state, сheck_total + cost)

    return state


# отображение результата
def print_results(purchase_results: tuple) -> None:
    print(f"Итоговая сумма покупки: {purchase_results[1]} руб.")
    print(f"Список покупок (Наименование, кол-во): {purchase_results[0]['items']}")
    print(f"Остаток на счете: {purchase_results[0]['money']} руб.")


# товары и их цена в магазине
items: dict = {
    "apples": 70,
    "wine": 300,
    "milk": 80,
    "chips": 100
}

# начальное состояние покупателя (список покупок и баланс на счете)
user: FunctionType = lambda balance: {"items": [], "money": balance}
# начальное состояние чека (руб.)
init_сheck_total: int = 0


if "__main__" == __name__:
    # пример 1
    purchase: State = (unit(State, user(2000))
                       >> buy(("apples", 2))
                       >> buy(("wine", 3))
                       >> buy(("chips", 10)))
    purchase_results: tuple = purchase(init_сheck_total)
    print_results(purchase_results)
    # Для покупки 'chips' в кол-ве 10 шт. недостаточно средств.
    # Итоговая сумма покупки: 1040 руб.
    # Список покупок (Наименование, кол-во): [('apples', 2), ('wine', 3)]
    # Остаток на счете: 960 руб.

    # пример 2
    purchase: State = (unit(State, user(2000))
                       >> buy(("milk", 10))
                       >> buy(("wine", 2))
                       >> buy(("chip", 10)))
    purchase_results: tuple = purchase(init_сheck_total)
    print_results(purchase_results)
    # Товара 'chip' нет в магазине.
    # Итоговая сумма покупки: 1400 руб.
    # Список покупок (Наименование, кол-во): [('milk', 10), ('wine', 2)]
    # Остаток на счете: 600 руб.

    # пример 3
    purchase: State = (unit(State, user(2000))
                       >> buy(("milk", 10))
                       >> buy(("wine", 2))
                       >> buy(("apples", 5)))
    purchase_results: tuple = purchase(init_сheck_total)
    print_results(purchase_results)
    # Итоговая сумма покупки: 1750 руб.
    # Список покупок (Наименование, кол-во): [('milk', 10), ('wine', 2), ('apples', 5)]
    # Остаток на счете: 250 руб.
