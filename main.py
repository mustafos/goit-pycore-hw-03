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

print(get_days_from_today("2026-10-10"))
print(get_days_from_today("2026-10-20"))