# Simple Calculator for Python by BingleyPro

menus = [0,1]

# Setup Main Menu
menus[0] = [
    [
        "1. Money Calculations",
        1
    ],
    [
        "2. Enable Developer Mode"
    ]
]

menus[1] = [
    ["1. Calculate GST for a value (10%)", -1, "ASK.Enter the value: ;value", "FINAL = value + getPercentageOf(value, 10)"],
    ["2. Calculate a price increase", -1, ""],
    ["3. Calculate a sale", -1, "ASK.Enter the value: ;value", "ASK.Enter the discount: ;discount", "FINAL = value - getPercentageOf(value, discont)"]
    #"Dev1. Calculate a percentage of a value added to that value",
    #"Dev2. Calculate a percentage of a value subtracted to that value"
]

# Calculate a percentage of a value
def getPercentageOf(value, percentage):
    return value * percentage / 100

# Get the value gotten before applying percentage (e.g 50 + 10% = 55, values given are 55 and 10%)
def backwardsGetPercentageOf(value, percentage):
   return (value * percentage) / (percentage + 1)

def askForInput(message, variable):
    return input(message)

print("\n\n\n\n\n--- Simple Calculator v1.0 ---")
def menu(menuNum):
    menuShown = "\n"
    theMenu = menus[menuNum]

    for menuItem in theMenu:
        menuShown += f"{menuItem[0]}\n"
    menuSelection = input(menuShown + "\nChoose a menu item: ")

    # --- Get the functions to apply --- #
    selectedItem = theMenu[int(menuSelection) - 1]

    if selectedItem[1] != -1:
        menu(selectedItem[1]) # Change Menu
    else:
        listItemCount = 0
        for listItem in selectedItem:
            if listItemCount == 0 | listItemCount == 1:
                listItemCount += 1
                return
            else:
                listItemCount += 1
                # listItem will have a list of comma seperated functions/variables

                
    
    if menuSelection == "1":
        GST = 10
    elif menuSelection == "2":
        GST = int(input("Enter a custom GST rate (without percentage sign): "))

    moneyBeforeGST = int(input("Enter a value: "))
    moneyAfterGST = moneyBeforeGST + getPercentageOf(moneyBeforeGST, GST)
    print(f"${moneyBeforeGST} is ${moneyAfterGST} after a GST of {GST}%.")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

menu(0)