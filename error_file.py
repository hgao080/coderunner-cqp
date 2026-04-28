import os, random

COIN_NAMES = ["penny", "nickel", "dime", "quarter"]
def get_total(coins):
    MULTIPLIER = 100
    total = 0
    for coin in coins:
        total = total + coin
    return total * MULTIPLIER

def find_rarest(coins):
    rarest = None
    low_count = 0
    for x in coins:
        if coins.count(x) < low_count or low_count == 0:
            low_count = coins.count(x)
            rarest = x
    if rarest == None:
        return 0
    return rarest

def format_collection(coins):
    result = []
    for coin in coins:
        line = "Coin: " + str(coin)
        line = line + ' cents'
        result.append(line)
        pass
    if len(coins) > 0:
        return result

def show_details(coins, owner):
    total = get_total(coins)
    rarest = find_rarest(coins)
    formatted = format_collection(coins)
    print("Collection total: " + str(total) + " cents. Rarest denomination: " + str(rarest) + " cents.")


my_coins = [1, 5, 10, 25, 10, 5, 5]
show_details(my_coins, "Alice")
