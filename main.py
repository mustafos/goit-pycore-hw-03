
import random
import re

from datetime import datetime, timedelta


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


def normalize_phone(phone_number):
    cleaned_phone = re.sub(r"\D", "", phone_number)

    if cleaned_phone.startswith("380"):
        return f"+{cleaned_phone}"

    return f"+38{cleaned_phone}"


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(
            user["birthday"], "%Y.%m.%d"
        ).date()

        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            # Handle February 29 in a non-leap year.
            birthday_this_year = birthday.replace(
                year=today.year, day=28
            )

        if birthday_this_year < today:
            try:
                birthday_this_year = birthday_this_year.replace(
                    year=today.year + 1
                )
            except ValueError:
                birthday_this_year = birthday_this_year.replace(
                    year=today.year + 1, day=28
                )

        if not (today <= birthday_this_year <= today + timedelta(days=6)):
            continue

        congratulation_date = birthday_this_year

        if congratulation_date.weekday() == 5:
            congratulation_date += timedelta(days=2)
        elif congratulation_date.weekday() == 6:
            congratulation_date += timedelta(days=1)

        upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
        })

    return upcoming_birthdays


if __name__ == "__main__":
    print("Task 1:")
    print(get_days_from_today("2026-10-10"))
    print(get_days_from_today("2026-10-20"))

    print("\nTask 2:")
    print(get_numbers_ticket(1, 49, 6))
    print(get_numbers_ticket(1, 10, 10))
    print(get_numbers_ticket(1, 5, 6))

    print("\nTask 3:")
    print(normalize_phone("067 123 4567"))
    print(normalize_phone("+380 50 123 4567"))
    print(normalize_phone("380501234567"))
    print(normalize_phone("(050) 888-9900"))

    print("\nTask 4:")
    users = [
        {"name": "John Doe", "birthday": "1985.10.16"},
        {"name": "Jane Smith", "birthday": "1990.10.18"},
        {"name": "Alex Brown", "birthday": "1992.10.20"},
    ]

    print(get_upcoming_birthdays(users))
