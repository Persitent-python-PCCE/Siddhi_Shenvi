from config.database import get_connection


class UserDAO:

    def email_exists(self, email):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT id
        FROM users
        WHERE email = %s
        """

        cursor.execute(query, (email,))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result is not None

    def add_user(self, user):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO users (name, email, password, role)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            user.name,
            user.email,
            user.password,
            user.role
        )

        cursor.execute(query, values)

        connection.commit()

        user.user_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return user

    def get_user_by_email(self, email):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT id, name, email, password, role
        FROM users
        WHERE email = %s
        """

        cursor.execute(query, (email,))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result