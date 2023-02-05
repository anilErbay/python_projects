### CAFE ###
# Order System

# MENU
menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'americano', "price": 2.50},
    3: {"name": 'flat white', "price": 2.79},
    4: {"name": 'cappuccino', "price": 3.50},
    5: {"name": 'cafe latte', "price": 3.99},
    6: {"name": 'mocha', "price": 3.69},
    7: {"name": 'macchiato', "price": 3.50},
    8: {"name": 'lemon cheesecake', "price": 3.80},
    9: {"name": 'apple pie', "price": 5.00},
    10: {"name": 'cupcake', "price": 3.00},
    11: {"name": 'brownie', "price": 5.49},
    12: {"name": 'cookie', "price": 3.99},
    13: {"name": 'profiterole', "price": 4.69},
    14: {"name": 'pain au chocolate', "price": 6.20},
}

# global underline
underline = '\33[4m'
end = '\033[0m'

# display the menu


def display_menu():
    print(f"{underline}|       ******* MENU *******        |{end}")
    for selection in menu:
        print(
            f"| {selection}. {menu[selection]['name'] :<18} | {menu[selection]['price'] :>9}€ |")
    print()

# take the order


def take_order():
    display_menu()
    order = []
    count = 1
    order_toggle = True
    print(f"{underline}Make selection below ,press 0(zero) to quit{end}")
    print()
    while (order_toggle):
        try:
            item = int(input("Select the menu item number " +
                       str(count) + " (from 1 to 14): "))
        except ValueError:
            print("Wrong input! Try again...")
        else:
            if item == 0:
                order_toggle = False
                break
            try:
                order.append(menu[item])
                count += 1
            except KeyError:
                print("Wrong input! Please make selection between 1 and 14")
    print()
    return order

# printing the order


def print_order(order):
    print(f"*** Order Details *** \n--> You have ordered {len(order)} items.")
    items = [item['name'] for item in order]
    print(f"--> {items}")
    print()
    return order


# calculate total

def calculate_total(order):
    subtotal = 0
    total = 0
    for i in order:
        subtotal += i['price']
    subtotal = round(subtotal, 2)
    print(f"Subtotal for the order: {subtotal}")
    # add tax

    def add_tax(subtotal):
        total = round(subtotal * 1.15, 2)
        print(f"Tax for the order: {round(subtotal * 0.15,2)}")
        print(f"{underline}Total price: {total} {end}")
        return total
    add_tax(subtotal)
    return total

# main function


def main():
    order = take_order()
    print_order(order)
    calculate_total(order)


if __name__ == "__main__":
    main()
