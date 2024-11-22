import mysql.connector

def show_table_structure():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password ="Chavela_1500!",
            database = "menagerie"
    )
        cursor = connection.cursor()
        cursor.execute("DESCRIBE pet")

        print("Structure of the pet table")
        for row in cursor.fetchall():
            print(row)
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
show_table_structure()
