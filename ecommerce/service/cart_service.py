from dao.cart_dao import CartDAO
from dao.product_dao import ProductDAO


class CartService:

    def __init__(self):

        self.cart_dao = CartDAO()
        self.product_dao = ProductDAO()


    def add_to_cart(self, user_id, product_id, quantity):

        if quantity <= 0:

            raise ValueError(
                "Quantity must be greater than zero."
            )


        product = self.product_dao.get_product_by_id(
            product_id
        )


        if product is None:

            raise ValueError(
                "Product not found."
            )


        product_id, name, price, stock, category_id = product


        if quantity > stock:

            raise ValueError(
                "Insufficient stock."
            )


        existing_item = self.cart_dao.get_cart_item(
            user_id,
            product_id
        )


        if existing_item:

            cart_id, user_id, product_id, current_quantity = (
                existing_item
            )

            new_quantity = current_quantity + quantity


            if new_quantity > stock:

                raise ValueError(
                    "Insufficient stock."
                )


            self.cart_dao.update_quantity(
                cart_id,
                new_quantity
            )


        else:

            self.cart_dao.add_to_cart(
                user_id,
                product_id,
                quantity
            )


        return True


    def remove_from_cart(self, user_id, product_id):

        rows_deleted = self.cart_dao.remove_from_cart(
            user_id,
            product_id
        )


        if rows_deleted == 0:

            raise ValueError(
                "Product is not in the cart."
            )


        return True


    def view_cart(self, user_id):

        return self.cart_dao.get_cart(user_id)


    def calculate_total(self, user_id):

        items = self.view_cart(user_id)

        total = 0


        for item in items:

            subtotal = item[5]

            total += subtotal


        return total


    def clear_cart(self, user_id):

        return self.cart_dao.clear_cart(user_id)