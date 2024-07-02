import calendar
import datetime
from datetime import date

def compute_leap_years(start_year,end_year):
    #This function computes the total additional days from leap years
    leap_year_check = start_year
    leap_year_days = 0
    if (start_year % 4 != 0 and end_year % 4 != 0):
        while leap_year_check <= end_year:
            if leap_year_check % 4 == 0:
                leap_year_days += 1
                leap_year_check += 1
            else:
                leap_year_check += 1
    elif (start_year % 4 != 0 and end_year % 4 == 0):
        if (end_month == 1 or (end_month == 2 and end_day < 29)):
            while leap_year_check < end_year:
                if leap_year_check % 4 == 0:
                    leap_year_days += 1
                    leap_year_check += 1
                else:
                    leap_year_check += 1
        elif ((end_month == 2 and end_day == 29) or end_month > 2):
            while leap_year_check <= end_year:
                if leap_year_check % 4 == 0:
                    leap_year_days += 1
                    leap_year_check += 1
                else:
                    leap_year_check += 1
    elif (start_year % 4 == 0 and end_year % 4 != 0):
        if (start_month > 2):
            leap_year_check += 1
            while leap_year_check <= end_year:
                if leap_year_check % 4 == 0:
                    leap_year_days += 1
                    leap_year_check += 1
                else:
                    leap_year_check += 1
        elif (start_month == 1) or (start_month == 2 and start_day <= 29):
            while leap_year_check <= end_year:
                if leap_year_check % 4 == 0:
                    leap_year_days += 1
                    leap_year_check += 1
                else:
                    leap_year_check += 1
    elif (start_year % 4 == 0 and end_year % 4 == 0):
        if ((start_month == 1) or (start_month == 2 and start_day <= 29)) and ((end_month == 2 and end_day == 29) or end_month > 2):
            while leap_year_check <= end_year:
                if leap_year_check % 4 == 0:
                    leap_year_days += 1
                    leap_year_check += 1
                else:
                    leap_year_check += 1
        elif (start_month > 2) and (end_month == 1 or (end_month == 2 and end_day < 29)):
            leap_year_check += 1
            while leap_year_check < end_year:
                if leap_year_check % 4 == 0:
                    leap_year_days += 1
                    leap_year_check += 1
                else:
                    leap_year_check += 1
        elif ((start_month == 1) or (start_month == 2 and start_day <= 29)) and (end_month == 1 or (end_month == 2 and end_day < 29)):
            while leap_year_check < end_year:
                if leap_year_check % 4 == 0:
                    leap_year_days += 1
                    leap_year_check += 1
                else:
                    leap_year_check += 1
        elif (start_month > 2) and ((end_month == 2 and end_day == 29) or (end_month > 2)):
            leap_year_check += 1
            while leap_year_check <= end_year:
                if leap_year_check % 4 == 0:
                    leap_year_days += 1
                    leap_year_check += 1
                else:
                    leap_year_check += 1
    return leap_year_days

def compute_total_days(start_month,start_day,start_year,end_month,end_day,end_year):
    #This function computes the total days between the start date and the end date
    leap_year_days = compute_leap_years(start_year,end_year)
    day_diff = end_day - start_day
    month_check = start_month
    month_diff = 0
    if end_month > month_check:
        while month_check < end_month:
            if month_check == 1 or month_check == 3 or month_check == 5 or month_check == 7 or month_check == 8 or month_check == 10 or month_check == 12:
                month_diff += 31
                month_check += 1
            elif month_check == 4 or month_check == 6 or month_check == 9 or month_check == 11:
                month_diff += 30
                month_check += 1
            else:
                month_diff += 28
                month_check += 1
    else:
        month_check -= 1
        while month_check >= end_month:
            if month_check == 1 or month_check == 3 or month_check == 5 or month_check == 7 or month_check == 8 or month_check == 10 or month_check == 12:
                month_diff -= 31
                month_check -= 1
            elif month_check == 4 or month_check == 6 or month_check == 9 or month_check == 11:
                month_diff -= 30
                month_check -= 1
            else:
                month_diff -= 28
                month_check -= 1
    if end_month == 2 and end_day == 29:
        return (end_year - start_year) * 365 + leap_year_days + day_diff + month_diff
    else:
        return (end_year - start_year) * 365 + 1 + leap_year_days + day_diff + month_diff

def identify_day(exact_date):
    #This function identifies what day of the week is the start date
    day = datetime.datetime.strptime(exact_date, "%d %m %Y").weekday() 
    return (calendar.day_name[day])
    #Code retrieved from: https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/#:~:text=Approach%20%231%20%3A%20Using%20weekday(),the%20day%20of%20the%20week.&text=The%20strftime()%20method%20takes,formatted%20string%20based%20on%20it.

def compute_weekdays(total_days,what_day):
    #This function computes the total weekdays and the total weekends in the total days
    if total_days % 7 == 1:
        if what_day == "Saturday" or what_day == "Sunday":
            total_weekdays = (total_days//7)*5
        else:
            total_weekdays = (total_days//7)*5 + 1
    elif total_days % 7 == 2:
        if what_day == "Saturday":
            total_weekdays = (total_days//7)*5
        elif what_day == "Sunday" or what_day == "Friday":
            total_weekdays = (total_days//7)*5 + 1
        else:
            total_weekdays = (total_days//7)*5 + 2
    elif total_days % 7 == 3:
        if what_day == "Saturday" or what_day == "Friday":
            total_weekdays = (total_days//7)*5 + 1
        elif what_day == "Sunday" or what_day == "Thursday":
            total_weekdays = (total_days//7)*5 + 2
        else:
            total_weekdays = (total_days//7)*5 + 3
    elif total_days % 7 == 4:
        if what_day == "Sunday" or what_day == "Wednesday":
            total_weekdays = (total_days//7)*5 + 3
        elif what_day == "Tuesday" or what_day == "Monday":
            total_weekdays = (total_days//7)*5 + 4
        else:
            total_weekdays = (total_days//7)*5 + 2
    elif total_days % 7 == 5:
        if what_day == "Monday":
            total_weekdays = (total_days//7)*5 + 5
        elif what_day == "Sunday" or what_day == "Tuesday":
            total_weekdays = (total_days//7)*5 + 4
        else:
            total_weekdays = (total_days//7)*5 + 3
    elif total_days % 7 == 6:
        if what_day == "Sunday" or what_day == "Monday":
            total_weekdays = (total_days//7)*5 + 5
        else:
            total_weekdays = (total_days//7)*5 + 4
    else:
        total_weekdays = (total_days//7)*5
    total_weekends = total_days - total_weekdays
    return total_weekdays, total_weekends

def compute_holidays(start_month,start_day,start_year,end_month,end_day,end_year):
    #This function computes holidays (New Year, Labor Day, All Saints' Day, Christmas Day) that land on weekdays
    SM,SD,SY,EM,ED,EY = start_month,start_day,start_year,end_month,end_day,end_year
    new_year = 0
    labor_day = 0
    halloween = 0
    christmas = 0
    while (SY != EY) or ((SY == EY and SM != EM and SD != ED) or (SY == EY and SM == EM and SD != ED) or (SY == EY and SM != EM and SD == ED)):
        if SM == 1 and SD == 1:
            if identify_day(f"{SD} {SM} {SY}") == "Saturday" or identify_day(f"{SD} {SM} {SY}") == "Sunday":
                SD += 1
            else:
                new_year += 1
                SD += 1
        elif SM == 5 and SD == 1:
            if identify_day(f"{SD} {SM} {SY}") == "Saturday" or identify_day(f"{SD} {SM} {SY}") == "Sunday":
                SD += 1
            else:
                labor_day += 1
                SD += 1
        elif SM == 11 and SD == 1:
            if identify_day(f"{SD} {SM} {SY}") == "Saturday" or identify_day(f"{SD} {SM} {SY}") == "Sunday":
                SD += 1
            else:
                halloween += 1
                SD += 1
        elif SM == 12 and SD == 25:
            if identify_day(f"{SD} {SM} {SY}") == "Saturday" or identify_day(f"{SD} {SM} {SY}") == "Sunday":
                SD += 1
            else:
                christmas += 1
                SD += 1
        else:
            if SM == 1 or SM == 3 or SM == 5 or SM == 7 or SM == 8 or SM == 10:
                if SD < 31:
                    SD += 1
                else:
                    SM += 1
                    SD -= 30
            elif SM == 2:
                if SY % 4 == 0:
                    if SD < 29:
                        SD += 1
                    else:
                        SM += 1
                        SD -= 28
                else:
                    if SD < 28:
                        SD += 1
                    else:
                        SM += 1
                        SD -= 27
            elif SM == 4 or SM == 6 or SM == 9 or SM == 11:
                if SD < 30:
                    SD += 1
                else:
                    SM += 1
                    SD -= 29
            else:
                if SD < 31:
                    SD += 1
                else:
                    SM -= 11
                    SD -= 30
                    SY += 1
    if identify_day(f"{ED} {EM} {EY}") == "Monday" or identify_day(f"{ED} {EM} {EY}") == "Tuesday" or identify_day(f"{ED} {EM} {EY}") == "Wednesday" or \
        identify_day(f"{ED} {EM} {EY}") == "Thursday" or identify_day(f"{ED} {EM} {EY}") == "Friday":
        if EM == 1 and ED == 1:
            new_year += 1
        elif EM == 5 and ED == 1:
            labor_day += 1
        elif EM == 11 and ED == 1:
            halloween += 1
        elif EM == 12 and ED == 25:
            christmas += 1
    return new_year,labor_day,halloween,christmas,new_year + labor_day + halloween + christmas

def compute_workdays(total_weekdays,total_holidays):
    #This function computes the total working days
    return total_weekdays - total_holidays

if __name__ == '__main__':
    
    #Inputs with checkpoint which validates if the value is an integer or not
    try:
        start_month = int(input("Enter start month: "))
    except ValueError:
        start_month_check = False
    else:
        start_month_check = True

    try:
        start_day = int(input("Enter start day: "))
    except ValueError:
        start_day_check = False
    else:
        start_day_check = True

    try:
        start_year = int(input("Enter start year: "))
    except ValueError:
        start_year_check = False
    else:
        start_year_check = True

    try:
        end_month = int(input("Enter end month: "))
    except ValueError:
        end_month_check = False
    else:
        end_month_check = True
    
    try:
        end_day = int(input("Enter end day: "))
    except ValueError:
        end_day_check = False
    else:
        end_day_check = True
    
    try:
        end_year = int(input("Enter end year: "))
    except ValueError:
        end_year_check = False
    else:
        end_year_check = True
    
    if start_month_check == False or start_day_check == False or start_year_check == False or \
        end_month_check == False or end_day_check == False or end_year_check == False:
        print("\nInvalid Input. Exiting Program.")
        raise SystemExit
    #Code retrieved from: https://stackoverflow.com/questions/36452105/python-user-input-data-type
    
    else:
    #Checkpoint which validates if the values are within the range and if the start date is correct
        if (1 <= start_month <= 12 and 1 <= end_month <= 12) and (1971 <= start_year <= 2020 and 1971 <= end_year <= 2020):
            if (start_month == 1 or start_month == 3 or start_month == 5 or start_month == 7 or start_month == 8 or start_month == 10 or start_month == 12):
                if (1 <= start_day <= 31):
                    start_date_valid = True
                else:
                    start_date_valid = False
            elif start_month == 2:
                if start_year % 4 == 0:
                    if (1 <= start_day <= 29):
                        start_date_valid = True
                    else:
                        start_date_valid = False
                else:
                    if (1 <= start_day <= 28):
                        start_date_valid = True
                    else:
                        start_date_valid = False
            else:
                if (1 <= start_day <= 30):
                    start_date_valid = True
                else:
                    start_date_valid = False
        else:
            print("\nInvalid Input. Exiting Program.")
            raise SystemExit
    
    #Another checkpoint which validates if the end date is correct
        if start_date_valid == True:
            if (end_month == 1 or end_month == 3 or end_month == 5 or end_month == 7 or end_month == 8 or end_month == 10 or end_month == 12):
                if (1 <= end_day <= 31):
                    end_date_valid = True
                else:
                    end_date_valid = False
            elif end_month == 2:
                if end_year % 4 == 0:
                    if (1 <= end_day <= 29):
                        end_date_valid = True
                    else:
                        end_date_valid = False
                else:
                    if (1 <= end_day <= 28):
                        end_date_valid = True
                    else:
                        end_date_valid = False
            else:
                if (1 <= end_day <= 30):
                    end_date_valid = True
                else:
                    end_date_valid = False
        else:
            print("\nInvalid Input. Exiting Program.")
            raise SystemExit

        if start_date_valid == True and end_date_valid == True:
            #Function calls
            total_days = compute_total_days(start_month,start_day,start_year,end_month,end_day,end_year)
            leap_year_days = compute_leap_years(start_year,end_year)
            what_day = identify_day(f"{start_day} {start_month} {start_year}")
            total_weekdays, total_weekends = compute_weekdays(total_days,what_day)
            new_year,labor_day,halloween,christmas,total_holidays = compute_holidays(start_month,start_day,start_year,end_month,end_day,end_year)
            working_days = compute_workdays(total_weekdays,total_holidays)
        else:
            print("\nInvalid Input. Exiting Program.")
            raise SystemExit

    #Outputs
    print(f"\ntotal days from start date to end date: {total_days}")
    print(f"\ntotal additional days from leap years: {leap_year_days}")
    print(f"\ntotal weekends: {total_weekends}")
    print(f"\ntotal days without weekends: {total_weekdays}")
    print(f"\nnew year holiday: {new_year}")
    print(f"labor day holiday: {labor_day}")
    print(f"all saints day holiday: {halloween}")
    print(f"christmas holiday: {christmas}")
    print(f"total holidays: {total_holidays}")
    print(f"\ntotal working days: {working_days}")