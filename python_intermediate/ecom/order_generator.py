import random
from datetime import datetime, timedelta
import json
import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)
store_name = config["store_name"]
minimum_order_amount = config["minimum_order_amount"]
maximum_order_amount = config["maximum_order_amount"]
default_currency = config["default_currency"]
allowed_statuses = config["allowed_statuses"]
num_orders = int(input("Enter number of orders: "))
products = [
    "Laptop",
    "Mobile Phone",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Headphones"
]
orders = []


for i in range(num_orders):
    order_id = 10001 + i
    customer_id = random.randint(1000, 9999)
    product = random.choice(products)
    quantity = random.randint(1, 5)
    unit_price = random.uniform(
        minimum_order_amount,
        maximum_order_amount
    )

    unit_price = round(unit_price, 2)
    total_amount = quantity * unit_price
    total_amount = round(total_amount, 2)
    status = random.choice(allowed_statuses)
    start_date = datetime(2026, 1, 1)
    random_days = random.randint(0, 364)
    random_date = start_date + timedelta(days=random_days)
    order_date = random_date.strftime("%Y-%m-%d")
    order = {
        "order_id": order_id,
        "customer_id": customer_id,
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_amount": total_amount,
        "status": status,
        "order_date": order_date
    }
    orders.append(order)

with open("orders.json", "w") as file:
    json.dump(orders, file, indent=4)


with open("orders.json", "r") as file:
    added_orders = json.load(file)

total_orders = len(added_orders)

total_sales = 0
delivered_orders = 0
cancelled_orders = 0
order_amounts = []


for order in added_orders:

    total_sales += order["total_amount"]

    order_amounts.append(order["total_amount"])

    if order["status"] == "Delivered":
        delivered_orders += 1

    if order["status"] == "Cancelled":
        cancelled_orders += 1

highest_order = max(order_amounts)
lowest_order = min(order_amounts)

print(f"\n==============={store_name} Order Report===============")

print(f"Total Orders       : {total_orders}")
print(f"Total Sales        : {default_currency} {total_sales:,.2f}")
print(f"Highest Order      : {default_currency} {highest_order:,.2f}")
print(f"Lowest Order       : {default_currency} {lowest_order:,.2f}")
print(f"Delivered Orders   : {delivered_orders}")
print(f"Cancelled Orders   : {cancelled_orders}")

print("\nOrder data saved successfully.")