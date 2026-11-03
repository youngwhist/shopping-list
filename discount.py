"""Скидки для списка покупок."""


def apply_discount(amount, percent):
    """Возвращает сумму со скидкой percent процентов."""
    if percent < 0 or percent > 100:
        raise ValueError("Скидка должна быть от 0 до 100 %")
    return round(amount * (1 - percent / 100), 2)


def card_discount(card):
    """Скидка в процентах по уровню карты (без карты — 0)."""
    levels = {'silver': 5, 'gold': 10}
    return levels.get(card, 0)
