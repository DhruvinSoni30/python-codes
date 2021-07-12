calculation_to_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    condition_check = num_of_days > 0
    print(type(condition_check))
    print(condition_check)
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}"
    elif num_of_days == 0:
        return  "You entered 0, please enter valid positive number!"
    else:
        return "Invalid input, Please enter valid input!"


user_input = input("Enter the number in days & I will convert it into hours!\n")

if user_input.isdigit():
    user_input_number = int(user_input)
    calculated_value = days_to_units(user_input_number)
    print(calculated_value)
else:
    print("Invalid input, Please enter a valid number!")
