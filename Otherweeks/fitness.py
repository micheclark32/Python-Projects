from datetime import datetime

# get users info


def main():

    gender = input("Please enter your gender (M or F): ")
    birthday = input("Please enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in pounds: "))
    inches = float(input("Enter your height in inches: "))
    pass


def compute_age(birthday):
    birthday = datetime.nowstrptime(birthday, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
            (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    kg = pounds * 0.45359237
    pass


def cm_from_in(inches):
    cm = inches * 2.54
    pass


def body_mass_index(kg, cm):
    bmi = 10000 * kg / pow(cm, 2)
    pass


def basal_metabolic_rate(gender, kg, cm, years):
    if(gender == 'M'):
        bmr = 88.362 + (13.397 * kg) + (4.799 * cm) - (5.677 * years)
    if(gender == 'F'):
        bmr = 447.593 + (9.247 * kg) + (3.098 * cm) - (4.330 * years)
    else:
        print("This is an invalid entry")


pass

main(compute_age, kg_from_lb, cm_from_in,
     body_mass_index, basal_metabolic_rate)
print()
