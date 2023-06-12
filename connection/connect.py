from config.configuration import config
import mysql.connector

def connect():
    try:
        params = config()

        print("Connecting to mySQL database...")
        # Connect to sql server
        conn = mysql.connector.connect(**params)

        # Show db details
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print("mySQL database version: ", str(db_version))
        cur.close()
    except (Exception, mysql.connector.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def connect_cursor():
    conn = None
    try:
        params = config()

        print("Connecting to mySQL database...")
        # Connect to sql server
        conn = mysql.connector.connect(**params)

        # Show db details
        cur = conn.cursor()
        return conn, cur
    except (Exception, mysql.connector.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    connect()
