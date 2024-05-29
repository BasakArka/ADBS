import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Basakarka"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute the SQL query to show databases
cursor.execute("USE")

# Fetch all rows from the result set
databases = cursor.fetchall()

# Print the names of all databases
for database in databases:
    print(database[0])