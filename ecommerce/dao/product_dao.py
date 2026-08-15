from config.database import get_connection


class ProductDAO:

    def add_product(self, product):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO products (name, price, stock, category_id)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            product.name,
            product.price,
            product.stock,
            product.category_id
        )

        cursor.execute(query, values)

        connection.commit()

        product.product_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return product

    def get_all_products(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            p.id,
            p.name,
            p.price,
            p.stock,
            c.name
        FROM products p
        LEFT JOIN categories c
        ON p.category_id = c.id
        """

        cursor.execute(query)

        products = cursor.fetchall()

        cursor.close()
        connection.close()

        return products

    def update_product(self, product):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        UPDATE products
        SET name = %s,
            price = %s,
            stock = %s,
            category_id = %s
        WHERE id = %s
        """

        values = (
            product.name,
            product.price,
            product.stock,
            product.category_id,
            product.product_id
        )

        cursor.execute(query, values)

        connection.commit()

        rows_updated = cursor.rowcount

        cursor.close()
        connection.close()

        return rows_updated

    
    def delete_product(self, product_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        DELETE FROM products
        WHERE id = %s
        """

        cursor.execute(query, (product_id,))

        connection.commit()

        rows_deleted = cursor.rowcount

        cursor.close()
        connection.close()

        return rows_deleted

    def category_exists(self, category_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT id
        FROM categories
        WHERE id = %s
        """

        cursor.execute(query, (category_id,))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result is not None

    def get_product_by_id(self, product_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT id, name, price, stock, category_id
        FROM products
        WHERE id = %s
        """

        cursor.execute(query, (product_id,))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def get_total_products(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT COUNT(*)
        FROM products
        """

        cursor.execute(query)

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result[0]


    def get_products_by_page(self, page, page_size):

        connection = get_connection()
        cursor = connection.cursor()

        offset = (page - 1) * page_size

        query = """
        SELECT
            p.id,
            p.name,
            p.price,
            p.stock,
            c.name
        FROM products p
        JOIN categories c
        ON p.category_id = c.id
        ORDER BY p.id
        LIMIT %s OFFSET %s
        """

        cursor.execute(
            query,
            (page_size, offset)
        )

        products = cursor.fetchall()

        cursor.close()
        connection.close()

        return products


    def get_total_products_by_category(self, category_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT COUNT(*)
        FROM products
        WHERE category_id = %s
        """

        cursor.execute(
            query,
            (category_id,)
        )

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result[0]


    def get_products_by_category(
        self,
        category_id,
        page,
        page_size
    ):

        connection = get_connection()
        cursor = connection.cursor()

        offset = (page - 1) * page_size

        query = """
        SELECT
            p.id,
            p.name,
            p.price,
            p.stock,
            c.name
        FROM products p
        LEFT JOIN categories c
        ON p.category_id = c.id
        WHERE p.category_id = %s
        ORDER BY p.id
        LIMIT %s OFFSET %s
        """

        cursor.execute(
            query,
            (
                category_id,
                page_size,
                offset
            )
        )

        products = cursor.fetchall()

        cursor.close()
        connection.close()

        return products

    def get_all_categories(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT id, name
        FROM categories
        ORDER BY id
        """

        cursor.execute(query)

        categories = cursor.fetchall()

        cursor.close()
        connection.close()

        return categories

    def update_stock(self, product_id, quantity):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        UPDATE products
        SET stock = stock - %s
        WHERE id = %s
        AND stock >= %s
        """

        cursor.execute(
            query,
            (
                quantity,
                product_id,
                quantity
            )
        )

        connection.commit()

        rows_updated = cursor.rowcount

        cursor.close()
        connection.close()

        return rows_updated