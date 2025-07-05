def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = 2025
if check_leap_year(year):
    print("Yes")
else:
    print("No")
# Year is muliple by 400
# year is multiple of 4 and not multiple 100
