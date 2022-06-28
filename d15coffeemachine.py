# from matplotlib.cbook import report_memory


# program requirements 
# 1. report
# 2. check resources sufficient?
# 3. process coins 
# 4. check trx successful?
# 5. make coffee 
# 6. reduce resources

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



while is_on:
    customer_order = input("What would you like? (espresso/latte/cappuccino):")
    if customer_order == "off":
        is_on = False
    elif customer_order == "report":
        print(f"Water:{resources['water']} ml")f
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[customer_order]

def is_resource_sufficient(order_ingredients):