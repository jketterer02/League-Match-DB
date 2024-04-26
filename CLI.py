import mysql.connector
import os

# Connect to the MySQL database
conn = mysql.connector.connect(host="localhost", user="root", password="password",ssl_disabled=True)

# Check if connection is established to the database
if conn.is_connected(): print("Connection established...")
# Create a cursor object to execute SQL queries
cursor = conn.cursor()
        

# Read SQL commands from file
with open("dbDDL.sql", 'r') as sql_file: sql_commands = sql_file.read()

cursor.execute(sql_commands, multi=True)
        
# Commit the transaction
conn.commit()

# Close the cursor
cursor.close()
# Close the connection
conn.close()