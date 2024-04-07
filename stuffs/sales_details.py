from datetime import datetime
import pg8000
import os
from dotenv import load_dotenv
import random

# sale_id
# customer_id
# sales_person_id
# Product_id
# quantity
# sale_date

# # Load environment variables from .env file
load_dotenv()

def generate_sale_data():
    conn = pg8000.connect(
        user=os.getenv('POSTGRE_USER'), 
        password=os.getenv('POSTGRE_PSWD'), 
        host='localhost', 
        port=5432, 
        database=os.getenv('POSTGRE_DB')
        )

    cursor = conn.cursor()
    cursor.execute("SELECT customer_id FROM public.customers")
    data =  cursor.fetchall()

    aa = random.choice(data)
    aa = str(aa)
    aa = int(aa[1:-1])
    customer = int(aa)
    conn.close()

    t = datetime.now()
    dating = t.strftime("%Y-%m-%dT%H:%M:%S")

    sh = str(random.randint(1000,9999))
    timepart = t.strftime("%H%j%M%S")
    sale = int(sh + timepart)
    salesperson = random.randrange(100,121)
    products = random.randrange(1001,1080)
    quantity = random.randrange(1,4)

    return sale, customer, salesperson, products, quantity, dating


print(generate_sale_data())
