MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def check_resources(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources.get(ingredient, 0) < amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True


def process_payment(drink):
    cost = MENU[drink]["cost"]
    print(f"This will be ${cost:.2f}.")
    pennies = int(input("How many pennies?   "))
    nickels = int(input("How many nickels?   "))
    dimes = int(input("How many dimes?     "))
    quarters = int(input("How many quarters?  "))
    total = pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25
    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = round(total - cost, 2)
    if change:
        print(f"Here is ${change:.2f} in change.")
    return True


def make_drink(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {drink}. Enjoy!")


def show_menu():
    print("\n--- MENU ---")
    for name, details in MENU.items():
        print(f"  {name.capitalize()}: ${details['cost']:.2f}")
    print()


def show_report():
    print(f"Water:  {resources['water']}ml")
    print(f"Milk:   {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit:.2f}")


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino) or 'menu'/'report'/'off': ").lower().strip()

    if user_choice == "off":
        print("Turning off. Goodbye!")
        break
    elif user_choice == "report":
        show_report()
    elif user_choice == "menu":
        show_menu()
    elif user_choice in MENU:
        if not check_resources(user_choice):
            continue
        if not process_payment(user_choice):
            continue
        profit += MENU[user_choice]["cost"]
        make_drink(user_choice)
    else:
        print(f"'{user_choice}' is not a valid option. Try again.")
