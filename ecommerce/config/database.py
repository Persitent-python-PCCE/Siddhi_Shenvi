import mysql.connector  


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Siddhi@28062004#",
        database="ecommerce_db"
    )

    return connection