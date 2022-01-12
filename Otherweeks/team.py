# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ").upper().strip()
    birthday = input("Please enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in pounds: "))
    inches = float(input("Enter your height in inches: "))
    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    # and basal_metabolic_rate functions as needed.
    age = compute_age(birthday)
    pounds_in_kg = kg_from_lb(pounds)
    inches_to_cm = cm_from_in(inches)
    b_m_i = body_mass_index(pounds_in_kg, inches_to_cm)
    b_m_r = basal_metabolic_rate(gender, pounds_in_kg, inches_to_cm, age)
    # Print the results for the user to see.
    print(f"Age (years): {age}")
    print(f"Weight (kg): {pounds_in_kg:.2f}")
    print(f"Height (cm): {inches_to_cm:.1f}")
    print(f"Body mass index: {b_m_i:.1f}")
    print(f"Basal metabolic rate (kcal/day): {b_m_r:.0f}")


def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
            (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    kg = pounds * 0.45359237
    return kg


def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    cm = inch * 2.54
    return cm


def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight/(height**2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    bmr = 0
    if(gender == 'M'):
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif(gender == 'F'):
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        print("This is an invalid entry")
    return bmr


# Call the main function so that
# this program will start executing.
main()
