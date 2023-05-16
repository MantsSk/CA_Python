import pickle


def save_cart(cart):
    with open("cart.pkl", "wb") as file:
        pickle.dump(cart, file)


def load_cart():
    try:
        with open("cart.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def add_item(cart):
    item_name = input("Enter the name of the item: ")
    item_price = float(input("Enter the price of the item: "))
    cart.append({"name": item_name, "price": item_price})
    print("Item added to the cart.")


def remove_item(cart):
    item_name = input("Enter the name of the item to remove: ")
    for item in cart:
        if item["name"] == item_name:
            cart.remove(item)
            print("Item removed from the cart.")
            return
    print("Item not found in the cart.")


def view_cart(cart):
    if len(cart) == 0:
        print("The cart is empty.")
    else:
        print("Items in the cart:")
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item['name']} - ${item['price']}")


def calculate_total(cart):
    total = sum(item["price"] for item in cart)
    print("Total cost of items: $" + str(total))


# Load cart data from file
cart = load_cart()

while True:
    print("Welcome to the Shopping Cart!")
    print("------------------------------")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Calculate total")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_item(cart)
        save_cart(cart)
    elif choice == "2":
        remove_item(cart)
        save_cart(cart)
    elif choice == "3":
        view_cart(cart)
    elif choice == "4":
        calculate_total(cart)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
