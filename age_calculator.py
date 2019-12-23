#Age Calculator---Python Script

from datetime import date
def check_birthdate(year, month, day):
    current_date = date.today()
    if current_date.year-year < 1:
        return False
    else:
        return True

def calculate_age(year, month, day):
    current_date = date.today()
    age_in_years = current_date.year - year - ((current_date.month, current_date.day) < (month, day))
    print("you are", age_in_years , "years old.")
    
    
year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))

if check_birthdate(year, month, day) == True:
    calculate_age(year, month, day)
else:
    print("Invalid Birthdate")