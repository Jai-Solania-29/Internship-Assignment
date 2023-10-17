from flask import Flask
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

def initialize_database():

    # Connection parameters
    db_endpoint = "database-1.cocsdsrhvwnt.ap-south-1.rds.amazonaws.com"
    db_name = "pythondb"
    db_user = "postgres"
    db_password = "123456789"

    # Establish a connection to the RDS instance
    conn = psycopg2.connect(
        host=db_endpoint,
        database=db_name,
        user=db_user,
        password=db_password
    )

    cursor = conn.cursor()

    create_table = """
    CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password_hash VARCHAR(255) NOT NULL
    );
    """

    cursor.execute(create_table)


    create_table_query = """
    INSERT INTO users (username, email, password_hash)
    VALUES
        ('jaideep_solania', 'jaideep2912@gmail.com', 'hashed_password'),
        ('hemant_sharma', 'hemantsw@gmail.com', 'another_hashed_password')
    """

    cursor.execute(create_table_query)

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)