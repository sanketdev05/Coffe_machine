# coffee machine using procedural method


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
    }
}

Money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
make_coffee = True


def checkresources():
    if choice == "report":
        for i in resources:
            if i == 'coffee':
                print(f"{i}: {resources['coffee']}g")
            else:
                print(f"{i}: {resources[i]}ml")
        print(f"Money: ${Money}")
        make_coffee = False
    else:
        for item in MENU[choice]['ingredients']:
            value1 = MENU[choice]['ingredients'][item]
            value2 = resources[item]
            resources[item] = value2 - value1

def is_resource_suff():
    for item in MENU[choice]['ingredients']:
        if MENU[choice]['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def coinoprator():
    print("Please insert coins")
    quaters = float(input("how many quaters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))

    inserted_coins = quaters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    cost = MENU[choice]['cost']
    if inserted_coins < cost:
        print("Sorry that's not enough money. Money refunded")
        make_coffee = False
    else:
        change = round(inserted_coins - cost, 2)
        print(f"Here is ${change} in change")
        print(f"Here is your {choice}. Enjoy")
        global Money
        Money += cost
    return inserted_coins


while make_coffee :
    choice = input("What would you like? (espresso, latte, cappuccino): ")
    if choice == 'off':
        make_coffee = False
    else:
        if choice == 'report':
            checkresources()
        else:
            if is_resource_suff():
                checkresources()
                coinoprator()
