# escape-room-lab/scripts/postgres_data_manipulation.py
import psycopg2

# Database connection parameters
conn_params = {
    'dbname': 'practice',
    'user': 'postgres',
    'password': 'yourpassword',
    'host': 'localhost',
    'port': 5432
}

# Connect to PostgreSQL
conn = psycopg2.connect(**conn_params)
cur = conn.cursor()

# Create profile table
create_table_query = '''
CREATE TABLE IF NOT EXISTS profile (
    id SERIAL PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    email VARCHAR
);
'''
cur.execute(create_table_query)
conn.commit()

# Import data from CSV
copy_data_query = '''
COPY profile (firstName, lastName, email)
FROM '/usr/share/data.csv'
DELIMITER ','
CSV HEADER;
'''
cur.execute(copy_data_query)
conn.commit()

# Ensure no data is overwritten while importing data2.csv
try:
    copy_data2_query = '''
    COPY profile (firstName, lastName, email)
    FROM '/usr/share/data2.csv'
    DELIMITER ','
    CSV HEADER;
    '''
    cur.execute(copy_data2_query)
except psycopg2.IntegrityError:
    conn.rollback()
    print("Data already exists. Skipping duplicate entries.")

# Query to confirm data import
cur.execute('SELECT * FROM profile;')
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
cur.close()
conn.close()
