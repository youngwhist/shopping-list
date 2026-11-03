"""Список покупок: добавление товаров и подсчёт суммы."""
from discount import apply_discount, card_discount


def add_item(items, name, price, quantity=1):
    """Добавляет товар в список и возвращает новый список."""
    return items + [{"name": name, "price": price, "quantity": quantity}]


def remove_item(items, name):
    """Удаляет товар по названию."""
    return [item for item in items if item["name"] != name]


def total(items):
    """Общая стоимость покупок в рублях."""
    return sum(item["price"] * item["quantity"] for item in items)


def checkout(items, card=None):
    """Итог к оплате с учётом скидки по карте."""
    return apply_discount(total(items), card_discount(card))


if __name__ == "__main__":
    basket = add_item([], "Хлеб", 45)
    basket = add_item(basket, "Молоко", 89, 2)
    basket = add_item(basket, "Сыр", 320)
    basket = remove_item(basket, "Сыр")
    print(f"Итого: {total(basket)} руб.")
    print(f"С картой gold: {checkout(basket, 'gold')} руб.")
