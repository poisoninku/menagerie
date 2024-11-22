import mysql.connector
def display_female_dogs():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Chavela_1500!",
            database="menagerie"    
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'")
        records = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        header = "| " + " | ".join(f"{col:<10}" for col in column_names) + " |"
        separator = "+" + "+".join("-" * (len(col) + 7) for col in column_names) + "+"
        print(separator)
        print(header)
        print(separator)
        for row in records:
            row_data = "| " + " | ".join(f"{str(val):<10}" if val is not None else "NULL      " for val in row) + " |"
            print(row_data)
        print(separator)
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
display_female_dogs()
