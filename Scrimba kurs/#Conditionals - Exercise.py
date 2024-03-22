def num_days(month):

    if month in {"jan", "mar", "may", "jul", "aug", "oct", "dec"}:
        print('number of days in',month,'is',31)
    elif month in {"apr", "jun", "sep", "nov"}:
        print('number of days in',month,'is',30)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    else:
        print("Error")


num_days('jul')
# optimize/shorten the code in the function
# try to reduce the number of conditionals 
