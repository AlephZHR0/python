from menu import MENU, resources

MONEY = 0
KEEP_RUNNING = True


def main():
    while KEEP_RUNNING:
        prompt_input()


def prompt_input():
    global KEEP_RUNNING
    user_input = input("What would you like? (espresso / latte / cappuccino): ").lower()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        make_cup_of(user_input)
    elif user_input == "report":
        report()
    elif user_input == "recharge":
        recharge()
    elif user_input == "off":
        KEEP_RUNNING = False
    else:
        print("please, use a valid command")
        prompt_input()


def make_cup_of(beverage):
    global MONEY
    if check_resources(beverage):
        if payment(beverage):
            preparing_receipt(beverage)
        else:
            return
    else:
        print("Ask for recharging resources to an employee")


def recharge():
    report()
    resources["water"] += int(input("How much of WATER you want to put?\n"))
    resources["milk"] += int(input("How much of MILK you want to put?\n"))
    resources["coffee"] += int(input("How much of COFFEE you want to put?\n"))
    report()


def report():
    print(f"""
Current amount of:
    - Water: {resources["water"]}ml
    - Milk: {resources["milk"]}ml
    - Coffee: {resources["coffee"]}g
    - Money: ${MONEY:.2f}    
    """)


def preparing_receipt(beverage):
    for ingredient in MENU[beverage]["ingredients"]:
        resources[ingredient] -= MENU[beverage]["ingredients"][ingredient]
    print(f"here is your {beverage}. Enjoy!")


def payment(beverage):
    approved = False
    global MONEY
    print("Please insert coins.")
    quarters = int(input("How many quarters?\n")) * 0.25
    dimes = int(input("How many dimes?\n")) * 0.10
    nickles = int(input("How many nickles?\n")) * 0.05
    pennies = int(input("How many pennies?\n")) * 0.01
    total_inserted = quarters + dimes + nickles + pennies
    if total_inserted < MENU[beverage]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        main()
    elif total_inserted == MENU[beverage]["cost"]:
        MONEY += total_inserted
        approved = True
    elif total_inserted > MENU[beverage]["cost"]:
        change = total_inserted - MENU[beverage]["cost"]
        total_inserted = total_inserted - change
        MONEY += total_inserted
        print(f"Here is {change:.2f} dollars in change.")
        approved = True
    return approved


def check_resources(beverage):
    enough_resources = True
    list_of_missing_resources = []
    for ingredient in MENU[beverage]["ingredients"]:
        if resources[ingredient] < MENU[beverage]["ingredients"][ingredient]:
            list_of_missing_resources.append(ingredient)
            enough_resources = False
    if enough_resources:
        return True
    else:
        return False


def missing_resources(beverage):
    list_of_missing_resources = []
    for ingredient in MENU[beverage]["ingredients"]:
        if resources[ingredient] < MENU[beverage]["ingredients"][ingredient]:
            list_of_missing_resources.append(ingredient)


main()
