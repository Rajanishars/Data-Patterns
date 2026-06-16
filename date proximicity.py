from datetime import datetime
from calendar import monthrange
def check_dates(date_str1, date_str2):
    d1 = datetime.strptime(date_str1, "%b %d %Y")
    d2 = datetime.strptime(date_str2, "%b %d %Y")
    d1, d2 = min(d1, d2), max(d1, d2)
    days_in_month = monthrange(d1.year, d1.month)[1]
    delta_days = (d2 - d1).days
    if delta_days == days_in_month and d1.day == d2.day:
        return "Exactly 1 month apart"
    elif delta_days < days_in_month:
        return "Less than 1 month apart"
    else:
        return "More than 1 month apart"
date1 = input().strip()
date2 = input().strip()
print(check_dates(date1, date2))
