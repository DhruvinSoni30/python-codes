calculation_to_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter valid positive number!")
    else:
        print("Invalid input, Please enter a valid number!")


user_input = input("Enter the number in days & I will convert it into hours!\n")

validate_and_execute()

