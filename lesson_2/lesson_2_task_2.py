
def is_year_leap(date):
    if date % 4 == 0:
        return True
    else:
        return False

def check_year(year):
    checked_year = f"Year {year}: {is_year_leap(year)}"
    print(checked_year)

check_year(2024)
