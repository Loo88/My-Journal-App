import psycopg2 
from psycopg2 import OperationalError
import os

def create_connection():
    try:
        DATABASE_URL=os.getenv('DB_URL')
        
        connection = psycopg2.connect(DATABASE_URL)

        print('Connection to postgreSQL DB successful!')

        return connection
    
    except OperationalError as e:
        print(f"The error '{e}' has occured.")
        return None
    
connection = create_connection()