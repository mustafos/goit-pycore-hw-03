import random

from datetime import datetime


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()

        difference = today - given_date

        return difference.days

    except (ValueError, TypeError):
        raise ValueError("Date must be a string in YYYY-MM-DD format")


def get_numbers_ticket(min_value, max_value, quantity):
    if not all(
        isinstance(value, int) and not isinstance(value, bool)
        for value in (min_value, max_value, quantity)
    ):
        return []

    if min_value < 1 or max_value > 1000 or min_value > max_value:
        return []

    if quantity < 1 or quantity > max_value - min_value + 1:
        return []

    numbers = random.sample(
        range(min_value, max_value + 1),
        quantity
    )

    return sorted(numbers)


if __name__ == "__main__":
    print(get_days_from_today("2026-10-10"))
    print(get_days_from_today("2026-10-20"))

    print(get_numbers_ticket(1, 49, 6))
    print(get_numbers_ticket(1, 10, 10))
    print(get_numbers_ticket(1, 5, 6))