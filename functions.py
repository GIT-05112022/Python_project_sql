from test_connection import *
grocery_store = sql_connection()

def calculate_discounted_cost(cost_per_kg, days_left, quantity_kg, item_type):
    if item_type == "grocery":
        if days_left >= 4 and days_left <= 7:
            expiry_discount = 0.20
        elif days_left >= 2 and days_left <= 3:
            expiry_discount = 0.50
        elif days_left <= 1:
            expiry_discount = 0.70
        else:
            expiry_discount = 0.0
    else:  
        if days_left >= 11 and days_left <= 30:
            expiry_discount = 0.20
        elif days_left >= 3 and days_left <= 10:
            expiry_discount = 0.50
        elif days_left <= 2:
            expiry_discount = 0.70
        else:
            expiry_discount = 0.0

    total_cost = quantity_kg * cost_per_kg
    expiry_discount_amount = total_cost * expiry_discount
    discounted_cost = total_cost - expiry_discount_amount
    return total_cost, expiry_discount, discounted_cost


def get_integer_input(prompt):
    while True:
        try:
            choice = int(input(prompt))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def process_items(table_name):
    cursor = grocery_store.cursor()
    query = f"SELECT * FROM gs.{table_name}"
    cursor.execute(query)

    item_names = []

    for row in cursor:
        item_id, item_name, item_type, cost, days_left_for_expiry = row
        item_names.append((item_id, item_name, item_type, cost, days_left_for_expiry))

    cursor.close()

    print(
        f"1. {table_name.capitalize()} items\n"
        "2. Non-grocery items"
    )

    choice1 = get_integer_input("Please select an option choice:")

    if choice1 == 1:
        print(f"Please select the {table_name} you want:")
        for idx, (item_id, item_name, _, _, _) in enumerate(item_names, start=1):
            print(f"{idx}. {item_name}")

        choice2 = get_integer_input(f"Please select a {table_name}: ")
        if 1 <= choice2 <= len(item_names):
            selected_item = item_names[choice2 - 1]
            item_name = selected_item[1]
            item_type = selected_item[2]
            cost_per_kg = float(selected_item[3])
            days_left = int(selected_item[4])
            print(f"Selected {table_name}: {item_name}")
            quantity_kg = float(input(f"Please enter quantity in units for {item_name}: "))

            total_cost, expiry_discount, discounted_cost = calculate_discounted_cost(cost_per_kg, days_left, quantity_kg, item_type)

            print("Do you have any additional coupons?")
            print("1. Yes")
            print("2. No")
            coupon_choice = get_integer_input("Please select an option: ")
            coupon_discount = 0  

            if coupon_choice == 1:
                coupon_id = get_integer_input("Please enter the coupon ID: ")
                cursor2 = grocery_store.cursor()
                query2 = f"SELECT Discount FROM gs.coupons WHERE Coupon_ID = {coupon_id}"
                cursor2.execute(query2)
                coupon_row = cursor2.fetchone()
                if coupon_row:
                    coupon_discount = float(coupon_row[0] * 0.01)
                    print(f"Applied coupon discount: {coupon_discount * 100:.2f}%")
                cursor2.close()

            if total_cost > 5000:
                print("Do you fall in any of the categories mentioned below:")
                print("1. Shop manager or A-grade Employee")
                print("2. Shop Staff")
                print("3. Normal customer")

                customer_choice = get_integer_input("Please select your category: ")
                customer_discount = 0  
                if customer_choice == 1:
                    customer_discount = 0.10
                elif customer_choice == 2:
                    customer_discount = 0.07
                else:
                    customer_discount = 0.05
                total_discount = coupon_discount + customer_discount
            else:
                total_discount = coupon_discount

            total_cost_after_discounts = total_cost * (1 - total_discount)
            discounted_cost_after_discounts = discounted_cost * (1 - total_discount)

            print(f"Cost per unit: Rs. {cost_per_kg:.2f}")
            print(f"Quantity: {quantity_kg} kg")
            print(f"Total cost before discount: Rs. {total_cost:.2f}")
            print(f"Total Discount (including coupon): {total_discount * 100:.2f}%")
            print(f"Total cost after all discounts: Rs. {total_cost_after_discounts:.2f}")
            print(f"Final cost after all discounts: Rs. {discounted_cost_after_discounts:.2f}")


