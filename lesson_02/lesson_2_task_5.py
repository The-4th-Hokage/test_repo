def month_to_season(a):
    if a in [1, 2, 12]:
        print('Winter')
    elif a in range(3, 6):
        print('Spring')
    elif a in range(6, 9):
        print('Summer')
    elif a in range(9, 12):
        print('Autumn')
    else:
        print("Please enter number from 1 to 12")



month_to_season(22)
month_to_season(12)