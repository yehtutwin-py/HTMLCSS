#display menu
ramen = {
    "shoyu": {
        "ingredients": {
            "noodles": 120,
            "broth": 300, 
            "pork": 50,
            "egg": 1,
        },
        "cost": 350
    },
    "miso": {
        "ingredients": {
            "noodles": 150,
            "broth": 350, 
            "pork": 70,
            "egg": 1,
        },
        "cost": 400
    },
    "tonkotsu": {
        "ingredients": {
            "noodles": 180,
            "broth": 400, 
            "pork": 90,
            "egg": 2,
        },
        "cost": 450
    }
}
resource = {
    "noodles": 1000,
    "broth": 1500,
    "pork": 600,
    "egg": 20,
    "money": 0
}
def resource_report():
    print(f"Noodles: {resource['noodles']}g")
    print(f"Broth: {resource['broth']}ml")
    print(f"Pork: {resource['pork']}g")
    print(f"Eggs: {resource['egg']}")
    print(f"Money: ¥{resource['money']}")
    
def check_resources(choice):
    for item in ramen[choice]["ingredients"]:
        if resource[item] < ramen[choice]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins(user_choice):
    print(f"Please insert coins for {user_choice} ramen.")
    total = 0
    coin_values = [500, 100, 50, 10, 5, 1]
    # check input for each coin type and calculate total not string and not negative
    for i in coin_values:
        while True:
            user_input = input(f"How many {i} yen coins?: ")
            check = int(user_input)
            if check < 0:
                print("Invalid input. Please enter a non-negative number.")
                continue
            total += check * i
            break
    return total

def make_ramen(choice):
    for item in ramen[choice]["ingredients"]:
        resource[item] -= ramen[choice]["ingredients"][item]

def menu():
    for item in ramen:
        print(f"{item.capitalize()} Ramen - ¥{ramen[item]['cost']}")
            
print("Welcome to Smart Ramen Machine!")
while True:
    user_choice = input("What would you like? (shoyu/miso/tonkotsu) : ")
    if user_choice=="off":
        break
    elif user_choice=="report":
        resource_report()
    elif user_choice=="menu":
        menu()
    else: 
        if user_choice in ramen:
            if check_resources(user_choice):
                total = process_coins(user_choice)
                if total >= ramen[user_choice]["cost"]:
                    make_ramen(user_choice)
                    print(f"Here is your change: ¥{total - ramen[user_choice]['cost']}")
                    print(f"Here is your {user_choice} ramen. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Please try again.")
        else:      
            print("Invalid selection. Try again.")