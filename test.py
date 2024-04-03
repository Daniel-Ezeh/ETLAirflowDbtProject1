# import mysql.connector
import os
from dotenv import load_dotenv
import pg8000


# # Load environment variables from .env file
load_dotenv()

# conn = mysql.connector.connect(
#     host="localhost",
#     user=os.getenv("MYSQL_USER"),
#     password=os.getenv('MYSQL_PSWD'),
#     database=os.getenv('MYSQL_DB')
# )


# cursor = conn.cursor()
# cursor.execute("SELECT * FROM ExampleTable")

# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# conn.close()


################################-----------------------------

# Create connection
conn = pg8000.connect(
    user=os.getenv('POSTGRE_USER'), 
    password=os.getenv('POSTGRE_PSWD'), 
    host='localhost', 
    port=5432, 
    database=os.getenv('POSTGRE_DB')
    )

cursor = conn.cursor()
cursor.execute("SELECT * FROM public.example_table")
for row in cursor.fetchall():
    print(row)
conn.close()


