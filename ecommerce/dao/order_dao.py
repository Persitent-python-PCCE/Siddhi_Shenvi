from config.database import get_connection


class OrderDAO:

    def create_order(self, user_id, total_amount):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO orders (user_id, total_amount, status)
        VALUES (%s, %s, %s)
        """

        values = (
            user_id,
            total_amount,
            "PLACED"
        )

        cursor.execute(query, values)

        connection.commit()

        order_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return order_id


    def add_order_item(
        self,
        order_id,
        product_id,
        quantity,
        price,
        subtotal
    ):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO order_items
        (order_id, product_id, quantity, price, subtotal)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            order_id,
            product_id,
            quantity,
            price,
            subtotal
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

        return True


    def get_orders_by_user(self, user_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            id,
            total_amount,
            status,
            created_at
        FROM orders
        WHERE user_id = %s
        ORDER BY id DESC
        """

        cursor.execute(
            query,
            (user_id,)
        )

        orders = cursor.fetchall()

        cursor.close()
        connection.close()

        return orders


    def get_order_items(self, order_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            oi.product_id,
            p.name,
            oi.quantity,
            oi.price
        FROM order_items oi
        JOIN products p
        ON oi.product_id = p.id
        WHERE oi.order_id = %s
        """

        cursor.execute(
            query,
            (order_id,)
        )

        items = cursor.fetchall()

        cursor.close()
        connection.close()

        return items

    def get_all_orders(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT id, user_id, total_amount, status
        FROM orders
        """

        cursor.execute(query)

        orders = cursor.fetchall()

        cursor.close()
        connection.close()

        return orders