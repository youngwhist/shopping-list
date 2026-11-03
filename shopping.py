"""Список покупок: добавление товаров и подсчёт суммы."""


def add_item(items, name, price, quantity=1):
    """Добавляет товар в список и возвращает новый список."""
    return items + [{"name": name, "price": price, "quantity": quantity}]


def remove_item(items, name):
    """Удаляет товар по названию."""
    return [item for item in items if item["name"] != name]


def total(items):
    """Общая стоимость покупок."""
    return sum(item["price"] * item["quantity"] for item in items)


if __name__ == "__main__":
    basket = add_item([], "Хлеб", 45)
    basket = add_item(basket, "Молоко", 89, 2)
    basket = add_item(basket, "Сыр", 320)
    basket = remove_item(basket, "Сыр")
    print(f"Итого: {total(basket)} руб.")
