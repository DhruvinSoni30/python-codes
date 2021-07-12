calculation_to_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}"


user_input = int(input("Enter the number in days & I will convert it into hours!\n"))
calculated_value = days_to_units(user_input)
print(calculated_value)

