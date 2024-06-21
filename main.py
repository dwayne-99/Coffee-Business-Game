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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
# Tracks profit, since this variable is in the global scope it has to be referenced using global keyword

def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Loop through each item in the ingredients dictionary
# Compare the required amount of the item with the available amount in resources
# If there's not enough of an item, print a message
# Return False, indicating insufficient resources
# If we've made it through the entire loop without returning False,
# it means we have enough of all ingredients

def process_coins():
    print("Please insert coins:")
    quarters = 0.25 * int(input("How many quarters?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    nickles = 0.05 * int(input("How many nickles?: "))
    pennies = 0.01 * int(input("How many pennies?: "))
    total = quarters + dimes + nickles + pennies
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Check if the money received is enough to cover the cost of the drink
# Calculate the change to be returned to the customer
# Round to 2 decimal places to avoid floating point precision issues
# Inform the customer about their change
# Declare that we'll be using the global 'profit' variable
# Add the cost of the drink to the total profit
# Return True to indicate a successful transaction
# If the money received is not enough, inform the customer
# Return False to indicate an unsuccessful transaction

def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

# Iterate through each ingredient required for the drink
# Subtract the required amount of each ingredient from the resources
# After preparing the drink, print a message to the user

def invest(amount, invest_resource):
    global profit
    print("$1 per 100ml/100g")

    if invest_resource not in resources:
        print(f"Invalid resource: {invest_resource}")
        return

    cost = int(amount)
    quantity = int(amount) * 100

    if profit >= cost:
        resources[invest_resource] += quantity
        profit -= cost
        print(f"Added {quantity}ml/g of {invest_resource}.")
        print(f"Current resources: {resources}")
        print(f"Remaining profit: ${profit}")
    else:
        print("Not enough profit to make this investment.")

# Declare that we'll be using the global 'profit' variable
# Inform the user about the pricing
# Check if the requested resource is valid (exists in the resources dictionary)
# Exit the function if the resource is invalid
# Convert amount to integer and calculate the cost and quantity
# Check if there's enough profit to make the investment
# Add the quantity to the resource
# Deduct the cost from the profit
# Inform the user about the transaction
# Inform the user if there's not enough profit

is_on = True

while is_on:
    print("Type 'profit' to see profits or 'invest' to invest profits")
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "profit":
        print(f"${profit}")
    elif choice == "invest":
        amount = input("How much do you want to invest: Type 1 for $1, or 3 for $3 ")
        invest_resource = input("Where would you like to invest your money: Water, Milk, or Coffee ").lower()
        invest(amount, invest_resource)
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

# Display options to the user
# Ask the user for their choice of drink
# Check the user's input and respond accordingly
# If the choice is "report", display the current resources and profit
# Allow the user to invest profits into resources using the invest function
# If the user chooses a drink process the drink order
# Check if there are enough resources to make the drink using the is_resource_sufficient function
# Process the payment using the process_coins function and save it to the payment variable
# Check if the money received is enough to cover the cost of the drink using the is_transaction
# If it is successful, make the coffee using the make_coffee function
