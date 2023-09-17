
def month_to_season(date):
    if date == 12 or date == 1 or date == 2:
        print("winter")
    elif date == 3 or date == 4 or date == 5:
        print("spring")
    elif date == 6 or date == 7 or date == 8:
        print("summer")
    else:
        print("autumn")
        
month_to_season(11)
    