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
# conn = pg8000.connect(
#     user=os.getenv('POSTGRE_USER'), 
#     password=os.getenv('POSTGRE_PSWD'), 
#     host='localhost', 
#     port=5432, 
#     database=os.getenv('POSTGRE_DB')
#     )

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM public.example_table")
# for row in cursor.fetchall():
#     print(row)
# conn.close()






from time import time
from datetime import datetime
import random

def generate_unique_key():
    timestamp = int(time() * 1000)  # Convert current time to milliseconds
    random_part = random.randint(0, 9999)  # Generate a random integer between 0 and 9999
    unique_key = f"{timestamp:03d}{random_part:04d}"  # Combine timestamp and random part
    return unique_key, timestamp

# Example usage
unique_key = generate_unique_key()
print(unique_key[0])
print(unique_key[1])
print(datetime.now())


