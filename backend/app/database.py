import psycopg2
from psycopg2 import OperationalError
import os

def connect_db():

    DATABASE_URL=os.getenv('DB_URL')

    conn = psycopg2.connect(DATABASE_URL)
    
    return conn

def create_tables():
    commands = (
        """"
        CREATE TABLE users(
        id SERIAL PRIMARY KEY,
        username VARCHAR (255) NOT NULL,
        password VARCHAR (255) NOT NULL
        )
        """,
        """
        CREATE TABLE entries(
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        text_content TEXT NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        nlp_results JSON,
        FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
    )

    conn = connect_db()
    cur = conn.cursor()
    for command in commands:
        cur.execute(command)
    conn.commit()
    cur.close()
    conn.close()