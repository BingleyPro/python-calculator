# Python Calculator by BingleyPro
# Feel free to use and modify this code as you see fit!

# -- FUNCTIONS --
# Calculate the percentage of a value
def get_percentage_of(value, percentage):
    return value * percentage / 100

# Calculate value before applying percentage
def backwards_get_percentage_of(value, percentage):
    return (value * percentage) / (percentage + 1)

def calculate_compound_interest(principal, rate, time, times_compounded):
    return principal * (1 + rate / (100 * times_compounded))**(times_compounded * time)

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def convert_currency(amount, rate):
    return amount * rate

def convert_length(value, from_unit, to_unit):
    conversions = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084
    }
    return value * conversions[to_unit] / conversions[from_unit]

def calculate_mortgage(principal, annual_rate, years):
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)

def calculate_tip(amount, percentage):
    return amount * percentage / 100

def calculate_calories(weight, height, age, gender, activity_level):
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr * activity_level

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

def calculate_age(birth_year, current_year):
    return current_year - birth_year

def calculate_loan(principal, rate, years):
    return calculate_mortgage(principal, rate, years)

def calculate_time_difference(time1, time2):
    h1, m1 = map(int, time1.split(":"))
    h2, m2 = map(int, time2.split(":"))
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    return abs(t2 - t1)

def convert_distance(value, from_unit, to_unit):
    return convert_length(value, from_unit, to_unit)

def convert_speed(value, from_unit, to_unit):
    conversions = {
        "km/h": 1,
        "mph": 0.621371,
        "m/s": 0.277778
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_area(value, from_unit, to_unit):
    conversions = {
        "square meters": 1,
        "square feet": 10.7639,
        "acres": 0.000247105
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_volume(value, from_unit, to_unit):
    conversions = {
        "liters": 1,
        "gallons": 0.264172,
        "cubic meters": 0.001
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        "kilograms": 1,
        "pounds": 2.20462,
        "ounces": 35.274
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_energy(value, from_unit, to_unit):
    conversions = {
        "joules": 1,
        "calories": 0.239006,
        "kilowatt-hours": 2.77778e-7
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_power(value, from_unit, to_unit):
    conversions = {
        "watts": 1,
        "horsepower": 0.00134102,
        "BTUs": 3.41214
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_pressure(value, from_unit, to_unit):
    conversions = {
        "pascals": 1,
        "bar": 1e-5,
        "psi": 0.000145038
    }
    return value * conversions[to_unit] / conversions[from_unit]

# -- SUBMENU FUNCTIONS --
def gst_menu():
    menuSelection = int(input("1. Calculate GST for a value at 10% rate \n2. Calculate a custom GST rate for a value\n3. Exit this menu\n"))
    print("\n")
    if menuSelection == 1:
        GST = 10
    elif menuSelection == 2:
        GST = int(input("Enter a custom GST rate (without percentage sign): "))
    elif menuSelection == 3:
        menu()
    else:
        print("Invalid selection. Please try again.")
        gst_menu()

    moneyBeforeGST = float(input("Enter a value: "))
    moneyAfterGST = moneyBeforeGST + (moneyBeforeGST * GST / 100)
    print(f"${moneyBeforeGST} is ${moneyAfterGST} after a GST of {GST}%.")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def percentage_menu():
    menuSelection = int(input("1. Calculate percentage of a value \n2. Calculate value before applying percentage\n"))
    print("\n")
    if menuSelection == 1:
        value = float(input("Enter the value: "))
        percentage = float(input("Enter the percentage: "))
        result = get_percentage_of(value, percentage)
        print(f"{percentage}% of {value} is {result}.")
    elif menuSelection == 2:
        value = float(input("Enter the value: "))
        percentage = float(input("Enter the percentage: "))
        result = backwards_get_percentage_of(value, percentage)
        print(f"The value before {percentage}% was applied to {value} is {result}.")
    else:
        print("Invalid selection. Please try again.")
        percentage_menu()
    
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def discount_menu():
    menuSelection = int(input("1. Calculate price after discount \n2. Calculate original price before discount\n"))
    print("\n")
    if menuSelection == 1:
        value = float(input("Enter the value: "))
        discount = float(input("Enter the discount: "))
        result = value - get_percentage_of(value, discount)
        print(f"{discount}% discount of {value} is {result}.")
    elif menuSelection == 2:
        value = float(input("Enter the value: "))
        discount = float(input("Enter the discount: "))
        result = backwards_get_percentage_of(value, discount)
        print(f"The value before {discount}% was applied to {value} is {result}.")
    else:
        print("Invalid selection. Please try again.")
        discount_menu()

    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def compound_interest_menu():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time (in years): "))
    times_compounded = int(input("Enter the number of times interest is compounded per year: "))
    amount = calculate_compound_interest(principal, rate, time, times_compounded)
    print(f"The amount after {time} years with an interest rate of {rate}% compounded {times_compounded} times per year is: ${amount:.2f}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def simple_interest_menu():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time (in years): "))
    interest = calculate_simple_interest(principal, rate, time)
    print(f"The simple interest for a principal amount of ${principal} at an interest rate of {rate}% over {time} years is: ${interest:.2f}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def bmi_menu():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def currency_converter_menu():
    amount = float(input("Enter the amount: "))
    rate = float(input("Enter the conversion rate: "))
    converted_amount = convert_currency(amount, rate)
    print(f"The converted amount is: ${converted_amount:.2f}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def length_converter_menu():
    value = float(input("Enter the value: "))
    from_unit = input("Enter the unit to convert from (meters, kilometers, miles, feet): ")
    to_unit = input("Enter the unit to convert to (meters, kilometers, miles, feet): ")
    converted_value = convert_length(value, from_unit, to_unit)
    print(f"The converted value is: {converted_value} {to_unit}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def mortgage_menu():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the number of years: "))
    monthly_payment = calculate_mortgage(principal, rate, years)
    print(f"Your monthly mortgage payment is: ${monthly_payment:.2f}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def tip_menu():
    amount = float(input("Enter the total amount: "))
    percentage = float(input("Enter the tip percentage: "))
    tip = calculate_tip(amount, percentage)
    print(f"The tip amount is: ${tip:.2f}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def calorie_menu():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    activity_level = float(input("Enter your activity level (1.2 for sedentary, 1.375 for light, 1.55 for moderate, 1.725 for active, 1.9 for very active): "))
    calories = calculate_calories(weight, height, age, gender, activity_level)
    print(f"Your daily caloric need is: {calories:.2f} calories")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def temperature_converter_menu():
    value = float(input("Enter the temperature value: "))
    from_unit = input("Enter the unit to convert from (Celsius, Fahrenheit, Kelvin): ")
    to_unit = input("Enter the unit to convert to (Celsius, Fahrenheit, Kelvin): ")
    converted_value = convert_temperature(value, from_unit, to_unit)
    print(f"The converted temperature is: {converted_value} {to_unit}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def age_menu():
    birth_year = int(input("Enter your birth year: "))
    current_year = int(input("Enter the current year: "))
    age = calculate_age(birth_year, current_year)
    print(f"Your age is: {age} years")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def loan_menu():
    principal = float(input("Enter the loan amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the number of years: "))
    monthly_payment = calculate_loan(principal, rate, years)
    print(f"Your monthly loan payment is: ${monthly_payment:.2f}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def time_difference_menu():
    time1 = input("Enter the first time (HH:MM): ")
    time2 = input("Enter the second time (HH:MM): ")
    difference = calculate_time_difference(time1, time2)
    hours = difference // 60
    minutes = difference % 60
    print(f"The time difference is: {hours} hours and {minutes} minutes")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def distance_converter_menu():
    value = float(input("Enter the distance value: "))
    from_unit = input("Enter the unit to convert from (meters, kilometers, miles, feet): ")
    to_unit = input("Enter the unit to convert to (meters, kilometers, miles, feet): ")
    converted_value = convert_distance(value, from_unit, to_unit)
    print(f"The converted distance is: {converted_value} {to_unit}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def speed_converter_menu():
    value = float(input("Enter the speed value: "))
    from_unit = input("Enter the unit to convert from (km/h, mph, m/s): ")
    to_unit = input("Enter the unit to convert to (km/h, mph, m/s): ")
    converted_value = convert_speed(value, from_unit, to_unit)
    print(f"The converted speed is: {converted_value} {to_unit}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def area_converter_menu():
    value = float(input("Enter the area value: "))
    from_unit = input("Enter the unit to convert from (square meters, square feet, acres): ")
    to_unit = input("Enter the unit to convert to (square meters, square feet, acres): ")
    converted_value = convert_area(value, from_unit, to_unit)
    print(f"The converted area is: {converted_value} {to_unit}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def volume_converter_menu():
    value = float(input("Enter the volume value: "))
    from_unit = input("Enter the unit to convert from (liters, gallons, cubic meters): ")
    to_unit = input("Enter the unit to convert to (liters, gallons, cubic meters): ")
    converted_value = convert_volume(value, from_unit, to_unit)
    print(f"The converted volume is: {converted_value} {to_unit}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def weight_converter_menu():
    value = float(input("Enter the weight value: "))
    from_unit = input("Enter the unit to convert from (kilograms, pounds, ounces): ")
    to_unit = input("Enter the unit to convert to (kilograms, pounds, ounces): ")
    converted_value = convert_weight(value, from_unit, to_unit)
    print(f"The converted weight is: {converted_value} {to_unit}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def energy_converter_menu():
    value = float(input("Enter the energy value: "))
    from_unit = input("Enter the unit to convert from (joules, calories, kilowatt-hours): ")
    to_unit = input("Enter the unit to convert to (joules, calories, kilowatt-hours): ")
    converted_value = convert_energy(value, from_unit, to_unit)
    print(f"The converted energy is: {converted_value} {to_unit}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def power_converter_menu():
    value = float(input("Enter the power value: "))
    from_unit = input("Enter the unit to convert from (watts, horsepower, BTUs): ")
    to_unit = input("Enter the unit to convert to (watts, horsepower, BTUs): ")
    converted_value = convert_power(value, from_unit, to_unit)
    print(f"The converted power is: {converted_value} {to_unit}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

def pressure_converter_menu():
    value = float(input("Enter the pressure value: "))
    from_unit = input("Enter the unit to convert from (pascals, bar, psi): ")
    to_unit = input("Enter the unit to convert to (pascals, bar, psi): ")
    converted_value = convert_pressure(value, from_unit, to_unit)
    print(f"The converted pressure is: {converted_value} {to_unit}")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

# -- MAIN MENU --
def menu():
    print("\n\n\n--- Simple Calculator v0.4 ---")
    menuSelection = int(input(
        "1. GST Calculator\n2. Percentage Calculator\n3. Discount Calculator\n4. Compound Interest Calculator\n"
        "5. Simple Interest Calculator\n6. BMI Calculator\n7. Currency Converter\n8. Length Converter\n"
        "9. Mortgage Calculator\n10. Tip Calculator\n11. Calorie Calculator\n12. Temperature Converter\n"
        "13. Age Calculator\n14. Loan Calculator\n15. Time Difference Calculator\n16. Distance Converter\n"
        "17. Speed Converter\n18. Area Converter\n19. Volume Converter\n20. Weight Converter\n"
        "21. Energy Converter\n22. Power Converter\n23. Pressure Converter\n24. Exit\n"))
    print("\n")
    if menuSelection == 1:
        gst_menu()
    elif menuSelection == 2:
        percentage_menu()
    elif menuSelection == 3:
        discount_menu()
    elif menuSelection == 4:
        compound_interest_menu()
    elif menuSelection == 5:
        simple_interest_menu()
    elif menuSelection == 6:
        bmi_menu()
    elif menuSelection == 7:
        currency_converter_menu()
    elif menuSelection == 8:
        length_converter_menu()
    elif menuSelection == 9:
        mortgage_menu()
    elif menuSelection == 10:
        tip_menu()
    elif menuSelection == 11:
        calorie_menu()
    elif menuSelection == 12:
        temperature_converter_menu()
    elif menuSelection == 13:
        age_menu()
    elif menuSelection == 14:
        loan_menu()
    elif menuSelection == 15:
        time_difference_menu()
    elif menuSelection == 16:
        distance_converter_menu()
    elif menuSelection == 17:
        speed_converter_menu()
    elif menuSelection == 18:
        area_converter_menu()
    elif menuSelection == 19:
        volume_converter_menu()
    elif menuSelection == 20:
        weight_converter_menu()
    elif menuSelection == 21:
        energy_converter_menu()
    elif menuSelection == 22:
        power_converter_menu()
    elif menuSelection == 23:
        pressure_converter_menu()
    elif menuSelection == 24:
        exit()
    else:
        print("Invalid selection. Please try again.")
        menu()
menu()