from flask import Flask
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

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

# Create a cursor object
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

# Execute SQL statements to create tables and other database objects

create_table_query = """
INSERT INTO users (username, email, password_hash)
VALUES
    ('jaideep_solania', 'jaideep2912@gmail.com', 'hashed_password'),
    ('hemant_sharma', 'hemantsw@gmail.com', 'another_hashed_password'),
;
"""
cursor.execute(create_table_query)

# Commit the changes and close the cursor and connection
conn.commit()
cursor.close()
conn.close()