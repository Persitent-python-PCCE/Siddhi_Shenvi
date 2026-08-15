from dao.order_dao import OrderDAO
from dao.cart_dao import CartDAO
from dao.product_dao import ProductDAO
from utils.backup import backup_orders

class OrderService:

    def __init__(self):

        self.order_dao = OrderDAO()
        self.cart_dao = CartDAO()
        self.product_dao = ProductDAO()


    def place_order(self, user_id):

        cart_items = self.cart_dao.get_cart(user_id)

        if not cart_items:

            raise ValueError(
                "Cart is empty."
            )

        total_amount = 0

        for product in cart_items:

            product_id = product[1]
            price = product[3]
            quantity = product[4]

            product = self.product_dao.get_product_by_id(
                product_id
            )

            if product is None:

                raise ValueError(
                    "Product not found."
                )

            stock = product[3]

            if quantity > stock:

                raise ValueError(
                    "Insufficient stock."
                )

            total_amount += price * quantity


        order_id = self.order_dao.create_order(
            user_id,
            total_amount
        )


        for product in cart_items:

            product_id = product[1]
            price = product[3]
            quantity = product[4]

            subtotal = price * quantity

            self.order_dao.add_order_item(
                order_id,
                product_id,
                quantity,
                price,
                subtotal
            )

            rows_updated = self.product_dao.update_stock(
                product_id,
                quantity
            )

            if rows_updated == 0:

                raise ValueError(
                    "Unable to update product stock."
                )


        self.cart_dao.clear_cart(user_id)

        return order_id


    def get_order_history(self, user_id):

        return self.order_dao.get_orders_by_user(
            user_id
        )


    def get_order_items(self, order_id):

        return self.order_dao.get_order_items(
            order_id
        )

    def backup_orders(self):

        orders = self.order_dao.get_all_orders()

        backup_orders(orders)