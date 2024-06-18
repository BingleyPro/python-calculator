# Simple Python Calculator by BingleyPro

# -- FUNCTIONS --
# Calculate the percentage of a value
def get_percentage_of(value, percentage):
    return value * percentage / 100

# Calculate value before applying percentage
def backwards_get_percentage_of(value, percentage):
    return (value * percentage) / (percentage + 1)

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

# -- MAIN MENU --
def menu():
    print("\n\n\n--- Simple Calculator v0.4 ---")
    menuSelection = int(input("1. GST Calculator \n2. Percentage Calculator\n3. Discount Calculator\n4. Quote of the Day\n5. Exit\n"))
    print("\n")
    if menuSelection == 1:
        gst_menu()
    elif menuSelection == 2:
        percentage_menu()
    elif menuSelection == 3:
        discount_menu()
    elif menuSelection == 4:
        input("Quote of the day: \"There is no quote\"")
    elif menuSelection == 5:
        exit()
    else:
        print("Invalid selection. Please try again.")
        menu()

menu()
