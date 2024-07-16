menu = {
    "aloo tikki": 5,
    "maharaja": 10,
    "mac special": 15
}

def calculate_bill(order):
    total_price = 0
    student_discount = 0
    delivery_charge = 0
    tip = 0

    for item, details in order.items():
        price = menu[item] * details["quantity"]
        total_price += price

        if details["is_student"]:
            student_discount += price * 0.20

        if details["delivery"]:
            delivery_charge += price * 0.05

        tip += details["tip"]

    total_price = total_price - student_discount + delivery_charge + tip

    return total_price

def print_bill(order, total_price):
    print("******************final bill***********************")
    print("sr.\tname\t\tprice\tquantity\ttotal_price")
    
    for idx, (item, details) in enumerate(order.items(), start=1):
        price = menu[item]
        total_item_price = price * details["quantity"]
        print(f"{idx}.\t{item}\t{price}$\t{details['quantity']}\t\t{total_item_price}$")

    print("---------------------------------------------------")
    print(f"\t\t\t\t{sum(menu[item] * details['quantity'] for item, details in order.items())}$")
    print(f"student discount 20%\t\t\t-{total_price - sum(menu[item] * details['quantity'] for item, details in order.items())}$")
    print(f"delivery charge 5%\t\t\t+{total_price * 0.05}$")
    print(f"tip\t\t\t\t\t\t{sum(details['tip'] for _, details in order.items())}$")
    print("---------------------------------------------------")
    print(f"total bill\t\t\t\t{total_price}$")
    print("\nThank you and come again")

def main():
    order = {}
    while True:
        print("Menu:")
        for idx, (item, price) in enumerate(menu.items(), start=1):
            print(f"{idx}. {item}\t{price}$")

        choice = input("Enter your choice (number) or 'done' to finish ordering: ")
        if choice.lower() == "done":
            break

        try:
            choice = int(choice)
            if choice < 1 or choice > len(menu):
                raise ValueError
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            continue

        item = list(menu.keys())[choice - 1]
        if item not in order:
            order[item] = {
                "quantity": 0,
                "is_student": False,
                "delivery": False,
                "tip": 0
            }

        quantity = int(input("Enter quantity: "))
        is_student = input("Are you a student? (yes/no): ").lower() == "yes"
        delivery = input("Do you want delivery? (yes/no): ").lower() == "yes"
        tip = int(input("Do you want to give tip? (2$/5$/10$): "))

        order[item]["quantity"] += quantity
        order[item]["is_student"] = is_student
        order[item]["delivery"] = delivery
        order[item]["tip"] += tip

    total_price = calculate_bill(order)
    print_bill(order, total_price)

if __name__ == "__main__":
    main()
