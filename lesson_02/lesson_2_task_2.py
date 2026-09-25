year = True

def is_year_leap(a):
    if (a % 4 == 0):
        year = True
        print("Year ", year_call,':', year)
        return year
    else:
        year = False
        print("Year ", year_call,':', year)
        return year


year_call = 2000

is_year_leap(year_call)