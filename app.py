from flask import Flask
import psycopg2

app = Flask(__name__)

# Connection parameters
db_endpoint = "database-1.cocsdsrhvwnt.ap-south-1.rds.amazonaws.com"
db_name = "pythondb"
db_user = "postgres"
db_password = "123456789"

def initialize_database():
    try:
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

        conn.commit()
        cursor.close()
        conn.close()

        return "Database initialized successfully"
    except psycopg2.Error as e:
        return f"Error initializing the database: {e}"

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/initialize')
def initialize():
    result = initialize_database()
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
