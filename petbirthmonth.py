import mysql.connector
def displayPetBirthAndMonth():
    try:
        connection = mysql.connector.connect(
            host="localhost", 
            user="root",          
            password="Chavela_1500!", 
            database="menagerie"  
        )
        cursor = connection.cursor()
        cursor.execute("""
            SELECT name, birth, MONTH(birth) AS birth_month
            FROM pet
        """)
        records = cursor.fetchall()
        column_names = ["Name", "Birth", "Birth(Month)"]
        header = "| " + " | ".join(f"{col:<15}" for col in column_names) + " |"
        separator = "+" + "+".join("-" * (len(col)+10) for col in column_names) + "+"
        print(separator)
        print(header)
        print(separator)
        for row in records:
            row_data = "| " + " | ".join(f"{str(val):<15}" if val is not None else "NULL            " for val in row[:-1]) + " | "
            row_data += f"{row[-1]:>15} |"
            print(row_data)
        print(separator)
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
displayPetBirthAndMonth()
