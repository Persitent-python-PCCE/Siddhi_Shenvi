import json
import os


def backup_orders(orders):

    os.makedirs("backup", exist_ok=True)

    data = []

    for order in orders:

        data.append({
            "order_id": order[0],
            "user_id": order[1],
            "total_amount": float(order[2]),
            "status": order[3]
        })

    with open("backup/orders.json", "w") as file:
        json.dump(data, file, indent=4)