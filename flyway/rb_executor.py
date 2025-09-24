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
    server = 'nhonlineordersql.database.windows.net'
    database = 'POC_DBAutomation'
    username = 'Flyway_User'
    password = '20@5_us3r'
    sql_file_path = 'C:/Users/TejaSurendar.Reddy/DB_Migrotron/flyway/rollback/rb_users_table.sql'

    apply_rollback_sql(server, database, username, password, sql_file_path)