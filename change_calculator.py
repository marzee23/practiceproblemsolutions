class NotEnoughChangeException(Exception):
    pass

def get_change(amount_owed, amount_paid):
    amount_of_change = amount_paid - amount_owed
    
    #if there's not enough change, i'm gonna throw an exception!
    if amount_of_change < 0:
        raise NotEnoughChangeException()
    
    #this list holds the value of the coin and it's string name
    coins = [(100, "dollars"), (25,"quarters"), 
        (10, "dimes"), (5, "nickels"), (1, "pennies")]

    #hold a list of strings like "n dollars" "n quarters" etc
    change_strings = [] 
    change_left = int(amount_of_change * 100)
    for coin_value, coin_name in coins:
        number_of_coins = int(change_left / coin_value)
        change_left = change_left - number_of_coins * coin_value
        change_strings.append("%d %s" % (number_of_coins, coin_name))

    return amount_of_change, change_strings
    
amount_owed = float(input("How much do you owe?: "))
amount_paid = float(input("How much are you paying?: "))

try:
    amount_of_change, change_strings = get_change(amount_owed, amount_paid)
    print("Your change is %s." % amount_of_change)
    print("That is " + ", ".join(change_strings))
except NotEnoughChangeException:
    print("Bitch better have my money!")
