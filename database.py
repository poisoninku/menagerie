import mysql.connector

def show_databases():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="Chavela_1500!"
        )
        if connection.is_connected():
            print("Connected to MySQL server")

            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")
            print("Databases available:")
            for db in cursor:
                print(f"- {db[0]}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")

show_databases()
