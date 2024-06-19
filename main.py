# Simple Python Calculator by BingleyPro

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

def interest_menu():
    menuSelection = int(input("1. Calculate simple interest \n2. Calculate compound interest\n"))
    print("\n")
    if menuSelection == 1:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the rate of interest: "))
        time = float(input("Enter the time period in years: "))
        result = (principal * rate * time) / 100
        print(f"The simple interest is {result}.")
    elif menuSelection == 2:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the rate of interest: "))
        time = float(input("Enter the time period in years: "))
        result = principal * (1 + rate / 100) ** time
        print(f"The compound interest is {result}.")
    else:
        print("Invalid selection. Please try again.")
        interest_menu()

def unit_conversion_menu():
    menuSelection = int(input("1. Convert length \n2. Convert weight\n 3. Convert volume\n"))
    print("\n")
    if menuSelection == 1:
        value = float(input("Enter the value: "))
        unit = int(input("Convert to: 1. cm 2. m 3. km\n"))
        if unit == 1:
            result = value * 100
            print(f"{value}m is {result}cm.")
        elif unit == 2:
            result = value / 100
            print(f"{value}cm is {result}m.")
        elif unit == 3:
            result = value / 1000
            print(f"{value}m is {result}km.")
        else:
            print("Invalid selection. Please try again.")
            unit_conversion_menu()
    elif menuSelection == 2:
        value = float(input("Enter the value: "))
        unit = int(input("Convert to: 1. g 2. kg 3. ton\n"))
        if unit == 1:
            result = value * 1000
            print(f"{value}kg is {result}g.")
        elif unit == 2:
            result = value / 1000
            print(f"{value}g is {result}kg.")
        elif unit == 3:
            result = value / 1000000
            print(f"{value}kg is {result}ton.")
        else:
            print("Invalid selection. Please try again.")
            unit_conversion_menu()
    elif menuSelection == 3:
        value = float(input("Enter the value: "))
        unit = int(input("Convert to: 1. ml 2. l 3. kl\n"))
        if unit == 1:
            result = value * 1000
            print(f"{value}l is {result}ml.")
        elif unit == 2:
            result = value / 1000
            print(f"{value}ml is {result}l.")
        elif unit == 3:
            result = value / 1000000
            print(f"{value}l is {result}kl.")
    else:
        print("Invalid selection. Please try again.")
        unit_conversion_menu()

    input("Press enter to continue or Ctrl+C to exit.")
    menu()

# -- MAIN MENU --
def menu():
    print("\n\n\n--- Simple Calculator v0.4 ---")
    menuSelection = int(input("1. GST Calculator \n2. Percentage Calculator\n3. Discount Calculator\n 4. Interest Calculator\n 5. Unit Conversion\n 6. Exit\n"))
    print("\n")
    if menuSelection == 1:
        gst_menu()
    elif menuSelection == 2:
        percentage_menu()
    elif menuSelection == 3:
        discount_menu()
    elif menuSelection == 4:
        interest_menu()
    elif menuSelection == 5:
        unit_conversion_menu()
    elif menuSelection == 6:
        exit()
    else:
        print("Invalid selection. Please try again.")
        menu()

menu()
