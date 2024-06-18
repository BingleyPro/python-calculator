# Simple GST Calculator for Python by BingleyPro
print("\n\n\n--- GST Calculator v1.1 ---")
def menu():
    menuSelection = int(input("1. Calculate GST for a value at 10% rate \n2. Calculate a custom GST rate for a value\n"))
    if menuSelection == 1:
        GST = 10
    else:
        GST = int(input("Enter a custom GST rate (without percentage sign): "))

    moneyBeforeGST = int(input("Enter a value: "))
    moneyAfterGST = moneyBeforeGST + (moneyBeforeGST * GST / 100)
    print(f"${moneyBeforeGST} is ${moneyAfterGST} after a GST of {GST}%.")
    input("Press enter to continue or Ctrl+C to exit.")
    menu()

menu()