from service.order_service import OrderService


class OrderController:

    def __init__(self):

        self.order_service = OrderService()


    def place_order(self, user):

        try:

            order_id = self.order_service.place_order(
                user.user_id
            )

            print(
                f"Order placed successfully!"
            )

            print(
                f"Order ID: {order_id}"
            )

        except ValueError as error:

            print(
                "Order failed:",
                error
            )


    def view_order_history(self, user):

        try:

            orders = (
                self.order_service
                .get_order_history(
                    user.user_id
                )
            )

            if not orders:

                print("No orders found.")
                return


            print("\n===== ORDER HISTORY =====")


            for order in orders:

                print(
                    f"\nOrder ID: {order[0]}"
                )

                print(
                    f"Total: ₹{order[1]}"
                )

                print(
                    f"Status: {order[2]}"
                )

                print(
                    f"Date: {order[3]}"
                )

                print("----------------------")


        except ValueError as error:

            print(
                "Error:",
                error
            )


    def backup_orders(self):

        try:

            self.order_service.backup_orders()

            print(
                "Orders backed up successfully!"
            )

        except Exception as error:

            print(
                "Backup failed:",
                error
            )