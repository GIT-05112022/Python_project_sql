import datetime
import mysql.connector

try:
    def sql_connection():
        connection = mysql.connector.connect(user='root', password='AA@#yu12', host='127.0.0.1', database='gs')
        return connection

except mysql.connector.Error as err:
    print("Error:", err)
