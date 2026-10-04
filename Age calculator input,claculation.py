# defining the for calculating the age, the function takes day
def calculate_age(day, month, year):
    # we are getting the current date using the today()
    today = date.today()
    # convering year, month and day into birthdate
    birthdate = date(year, month, day)
    # calculating the age 
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    # return the age value
    return age