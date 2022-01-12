import csv


def main():
    students_dict = csv_to_dict()
    keep_asking = True
    while (keep_asking):
        user_input = input("Please enter I-Number (q to quit): ").lower()
        if user_input == "q":
            keep_asking = False
            return

        if user_input in students_dict:
            student_name = students_dict[user_input]
            print(f"This student is {student_name}")
        else:
            print("Student does not exist.")


def csv_to_dict():

    data = {}
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = row["I-Number"]
            value = row["Name"]
            data[key] = value
    print(data)

    return data


main()
