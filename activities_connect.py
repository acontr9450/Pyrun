import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

def prepare_sql_statement(sql_statement):
    return sql.SQL(sql_statement)

def execute_prepared_statement(db_config, prepared_statement):
    conn = False
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(prepared_statement)
        conn.commit()
        
        # Fetch and return the results if it's a SELECT statement
        if prepared_statement.as_string(conn).strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        
        else:
            return cursor.rowcount  # Number of rows affected for INSERT, UPDATE, DELETE

    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return None
    
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

def deallocate_prepared_sql(db_config, prepared_name):
    deallocate_sql = f"DEALLOCATE {prepared_name};"
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(deallocate_sql)
        conn.commit()

    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return None
    
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

load_dotenv()

dbconfig = {
    'dbname': 'casaos',
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': '192.168.1.45',
    'port': '5432'
}

prepare_insert = """
INSERT INTO activities (
    id, name, distance, moving_time, elapsed_time, total_elevation_gain, 
    elev_high, elev_low, avg_heartrate, gear_id, type, sport_type, start_date
) VALUES (
    1, 'Morning Run', 5000.0, 1800.0, 2000.0, 50.0, 
    150.0, 100.0, 140.0, 'gear123', 'Run', 'Road Running', '2024-06-14'
);
"""

prepare_select = """
SELECT * FROM activities;
"""

prepared_statement = prepare_sql_statement(prepare_select)
result = execute_prepared_statement(dbconfig, prepared_statement)
print(f"Results: {result}")
#print(f"Rows affected: {result}")




