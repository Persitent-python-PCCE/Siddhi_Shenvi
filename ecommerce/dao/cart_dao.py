from config.database import get_connection


class CartDAO:

    def add_to_cart(self, user_id, product_id, quantity):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO carts (user_id, product_id, quantity)
        VALUES (%s, %s, %s)
        """

        values = (
            user_id,
            product_id,
            quantity
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

        return True


    def get_cart_item(self, user_id, product_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT id, user_id, product_id, quantity
        FROM carts
        WHERE user_id = %s
        AND product_id = %s
        """

        cursor.execute(
            query,
            (user_id, product_id)
        )

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result


    def update_quantity(self, cart_id, quantity):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        UPDATE carts
        SET quantity = %s
        WHERE id = %s
        """

        values = (
            quantity,
            cart_id
        )

        cursor.execute(
            query,
            values
        )

        connection.commit()

        rows_updated = cursor.rowcount

        cursor.close()
        connection.close()

        return rows_updated


    def remove_from_cart(self, user_id, product_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        DELETE FROM carts
        WHERE user_id = %s
        AND product_id = %s
        """

        cursor.execute(
            query,
            (user_id, product_id)
        )

        connection.commit()

        rows_deleted = cursor.rowcount

        cursor.close()
        connection.close()

        return rows_deleted


    def get_cart(self, user_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            c.id,
            c.product_id,
            p.name,
            p.price,
            c.quantity,
            (p.price * c.quantity) AS subtotal
        FROM carts c
        JOIN products p
        ON c.product_id = p.id
        WHERE c.user_id = %s
        """

        cursor.execute(
            query,
            (user_id,)
        )

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result


    def clear_cart(self, user_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        DELETE FROM carts
        WHERE user_id = %s
        """

        cursor.execute(
            query,
            (user_id,)
        )

        connection.commit()

        rows_deleted = cursor.rowcount

        cursor.close()
        connection.close()

        return rows_deleted