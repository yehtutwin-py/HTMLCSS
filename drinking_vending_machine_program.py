resources = {
    "water": 1000,
    "Fruit": 500,
    "sugar": 200,
    "ice": 300,
}
money_earned = 0
drink = {
    "Lemon" : {
        "requirements" :{
            "water":200,
            "Fruit":80,
            "sugar":20,
            "ice":50
        },
        "cost": 200
    },
    "Strawberry" : {
        "requirements" :{
            "water":250,
            "Fruit":100,
            "sugar":25,
            "ice":60
        },
        "cost": 250
    },
    "Pineapple" : {
        "requirements" :{
            "water":300,
            "Fruit":120,
            "sugar":30,
            "ice":70
        },
        "cost": 300
    }
}
def report_resource(resource):
    print(f"Water: {resource['water']}ml")
    print(f"Fruit: {resource['Fruit']}g")
    print(f"Sugar: {resource['sugar']}g")
    print(f"Ice: {resource['ice']}g")
    print(f"Money: ${money_earned}")

def is_resource_sufficient(order_requirements):
    for item in order_requirements:
        if order_requirements[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def resource_deduction(drink, order_requirements):
    for item in order_requirements:
        resources[item] -= order_requirements[item]
    print(f"Preparing your drink...\nHere is your {drink} juice. Enjoy!\n")

def calculate_total_coins():
    coins = [500, 100, 50, 10, 5, 1]; total = 0
    for coin in coins:
        while True:
            user_input = input(f"How many {coin} yen coins?: ").strip()
            if not user_input.isdigit():
                print("Invalid input. Please enter a non-negative number.")
                continue
            check = int(user_input)
            if check < 0:
                print("Invalid input. Please enter a non-negative number.")
                continue
            total += check * coin
            break
    return total

def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Return change: \nHere is ¥{change}.")
        global money_earned
        money_earned += drink_cost
        return True
    else:
        return False

is_on = True
while is_on:  
    print("Welcome to Smart Drink Machine!! Menu: \n1. Lemon Juice - ¥200\n2. Strawberry Juice - ¥250 \n3. Pineapple Juice - ¥300 \n")
    user_input = input("What would you like? (Lemon/Strawberry/Pineapple): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        report_resource(resources)
    elif user_input in drink:
        order = drink[user_input]
        if is_resource_sufficient(order["requirements"]):
            print("Please insert coins")
            payment = calculate_total_coins()
            if transaction_successful(payment, order["cost"]):
                resource_deduction(user_input, order["requirements"])
            else:
                print("Sorry that's not enough money. Money refunded.\n")
    else:
        print("Invalid selction. Please try again\n")