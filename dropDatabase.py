import mysql.connector
def dropDatabase():
    try:
        connection = mysql.connector.connect(
            host="localhost",  
            user="root",          
            password="Chavela_1500!"  
        )
        cursor = connection.cursor()
        cursor.execute("DROP DATABASE IF EXISTS menagerie")
        print("Database 'menagerie' dropped successfully.")
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
dropDatabase()
