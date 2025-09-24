import pyodbc

def apply_rollback_sql(server, database, username, password, sql_file_path):
    try:
        # Establish connection to the SQL Server database
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        cursor = conn.cursor()

        # Read rollback SQL script
        with open(sql_file_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()

        # Split script into individual statements
        # SQL Server uses "GO" as batch separator, split by that
        commands = sql_script.split('GO')

        for command in commands:
            command = command.strip()
            if command:
                cursor.execute(command)
        
        # Commit the rollback transaction
        conn.commit()

        print("Rollback script applied successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    # Replace these parameters with your actual DB connection info and rollback file path
    server = os.getenv('server')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
    sql_file_path = os.getenv('sql_file_path')

    apply_rollback_sql(server, database, username, password, sql_file_path)