# Simple Calculator for Python by BingleyPro

# Calculate the percentage of a value
def get_percentage_of(value, percentage):
    return value * percentage / 100

# Calculate value before applying percentage
def backwards_get_percentage_of(value, percentage):
    return (value * percentage) / (percentage + 1)

# Handle Input
def ask_for_input(message):
    return input(message)

# Main menu and submenus definition
menus = [
    [
        {"text": "1. Money Calculations", "action": 1},
        {"text": "2. Enable Developer Mode"}
    ],
    [
        {"text": "1. Calculate GST for a value (10%)", "action": -1,
         "input_prompt": "Enter the value: ",
         "action_code": "value + get_percentage_of(value, 10)"},
        {"text": "2. Calculate a price increase", "action": -1,
         "input_prompt": "Enter the original price: ",
         "action_code": "value + value * int(ask_for_input('Enter the increase amount: '))"},
        {"text": "3. Calculate a sale", "action": -1,
         "input_prompts": ["Enter the original price: ", "Enter the discount percentage: "],
         "action_code": "value - get_percentage_of(value, discount)"},
        {"text": "4. Basic Arithmetic Operations", "action": 2},
        {"text": "5. Exit"}
    ],
    [
        {"text": "1. Addition", "action": -1,
         "input_prompts": ["Enter the first number: ", "Enter the second number: "],
         "action_code": "value + ask_for_input('Enter the second number: ')"},
        {"text": "2. Subtraction", "action": -1,
         "input_prompts": ["Enter the first number: ", "Enter the second number: "],
         "action_code": "value - ask_for_input('Enter the second number: ')"},
        {"text": "3. Multiplication", "action": -1,
         "input_prompts": ["Enter the first number: ", "Enter the second number: "],
         "action_code": "value * ask_for_input('Enter the second number: ')"},
        {"text": "4. Division", "action": -1,
         "input_prompts": ["Enter the dividend: ", "Enter the divisor: "],
         "action_code": "value / ask_for_input('Enter the divisor: ')"},
        {"text": "5. Back to Previous Menu", "action": 1}
    ]
]

# Display the menu
def show_menu(menu_num):
    print("\n\n\n\n\n--- Simple Calculator v1.0 ---")
    while True:
        menu_shown = "\n"
        for item in menus[menu_num]:
            menu_shown += item["text"] + "\n"
        
        menu_selection = input(menu_shown + "\nChoose a menu item: ")

        try:
            selected_item = menus[menu_num][int(menu_selection) - 1]

            if selected_item["action"] != -1:
                show_menu(selected_item["action"])  # Change Menu
            else:
                if "input_prompt" in selected_item:
                    value = float(input(selected_item["input_prompt"]))
                elif "input_prompts" in selected_item:
                    inputs = []
                    for prompt in selected_item["input_prompts"]:
                        inputs.append(float(input(prompt)))
                    value = inputs[0]
                    discount = inputs[1]

                # Execute the action defined for the menu item
                if "action_code" in selected_item:
                    if isinstance(selected_item["action_code"], str):
                        result = eval(selected_item["action_code"])
                        print(f"Result: {result}")
                    elif callable(selected_item["action_code"]):
                        selected_item["action_code"](value, discount)
                
                if menu_num == 0:
                    input("Press enter to continue or Ctrl+C to exit.")
                show_menu(menu_num)

        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid menu option.")

# Function to perform addition
def perform_addition(value1, value2):
    result = value1 + value2
    print(f"Addition Result: {result}")

# Function to perform subtraction
def perform_subtraction(value1, value2):
    result = value1 - value2
    print(f"Subtraction Result: {result}")

# Function to perform multiplication
def perform_multiplication(value1, value2):
    result = value1 * value2
    print(f"Multiplication Result: {result}")

# Function to perform division
def perform_division(value1, value2):
    if value2 == 0:
        print("Cannot divide by zero.")
    else:
        result = value1 / value2
        print(f"Division Result: {result}")

# Adding the arithmetic operation functions to the submenu
menus[2][0]["action_code"] = perform_addition
menus[2][1]["action_code"] = perform_subtraction
menus[2][2]["action_code"] = perform_multiplication
menus[2][3]["action_code"] = perform_division

# Initial call to start the program
show_menu(0)