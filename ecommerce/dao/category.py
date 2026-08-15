class CategoryDAO:

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