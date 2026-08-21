from service.cart_service import CartService


class CartController:

    def __init__(self):

        self.cart_service = CartService()


    def add_to_cart(self, user):

        try:

            product_id = int(
                input("Enter product ID: ")
            )

            quantity = int(
                input("Enter quantity: ")
            )


            self.cart_service.add_to_cart(
                user.user_id,
                product_id,
                quantity
            )


            print(
                "Product added to cart successfully."
            )


        except ValueError as error:

            print("Error:", error)


    def remove_from_cart(self, user):

        try:

            product_id = int(
                input("Enter product ID: ")
            )


            self.cart_service.remove_from_cart(
                user.user_id,
                product_id
            )


            print(
                "Product removed from cart successfully."
            )


        except ValueError as error:

            print("Error:", error)


    def view_cart(self, user):

        try:

            items = self.cart_service.view_cart(
                user.user_id
            )


            if not items:

                print("Your cart is empty.")

                return


            print("\n===== YOUR CART =====")


            for item in items:

                print(
                    f"Product ID: {item[1]}"
                )

                print(
                    f"Product: {item[2]}"
                )

                print(
                    f"Price: ₹{item[3]:.2f}"
                )

                print(
                    f"Quantity: {item[4]}"
                )

                print(
                    f"Subtotal: ₹{item[5]:.2f}"
                )

                print("---------------------")


            total = self.cart_service.calculate_total(
                user.user_id
            )


            print(
                f"Total: ₹{total:.2f}"
            )


        except ValueError as error:

            print("Error:", error)


    def clear_cart(self, user):

        try:

            rows_deleted = self.cart_service.clear_cart(
                user.user_id
            )


            if rows_deleted == 0:

                print("Cart is already empty.")


            else:

                print(
                    "Cart cleared successfully."
                )


        except ValueError as error:

            print("Error:", error)