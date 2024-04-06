import requests
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook



default_args = {
    'owner':"Dan4sure",
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'catchup': True
}

SQL = '''insert into 
  customers (
    customer_id,
    firstname, 
    lastname, 
    gender, 
    email, 
    phone, 
    address, 
    country,
    date_added
  )
values
  (%s, %s, %s, %s, %s, %s, %s, %s, %s);
'''


# def querying_postgres():
#     hook = PostgresHook(postgres_conn_id='postgres_localhost')
#     conn = hook.get_conn()
#     cursor = conn.cursor()
#     hook.run(sql, parameters=values)
#     cursor.execute("SELECT * FROM public.example_table")
#     result = hook.get_records(sql="SELECT * FROM public.example_table")
#     for row in result:
#         print(row)
#     conn.close()


def fetch_data():
    """
    Fetch weather data from the API for a specific city.
    """
    # Endpoint URL for the weather API
    url = f'https://randomuser.me/api/?results=1'
    try:
        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status() 

        data = response.json()

        # myDict = dict(
        # firstname = data['results'][0]['name']['first'],
        # lastname = data['results'][0]['name']['last'],
        # gender = data['results'][0]['gender'],
        # email = data['results'][0]['email'],
        # phone = data['results'][0]['phone'],
        # address = str(data['results'][0]['location']['street']['number']) + " " + data['results'][0]['location']['street']['name'] + "," + " " + data['results'][0]['location']['city'] + "," + " " + data['results'][0]['location']['state'],
        # country = data['results'][0]['location']['country'],
        # )
        return data
    

    except requests.exceptions.RequestException as e:
        # Handle connection errors or bad responses
        print("Error getting user:", e)
        return None




def insert_data_to_postgres(**context):
    data = context['task_instance'].xcom_pull(task_ids='fetch_data_task')
    hook = PostgresHook(postgres_conn_id='postgres_localhost')
    
    for USER in data:
        # Insert each record into the database
        sql = SQL
        values = (
            USER['firstname'],
            USER['lastname'],
            USER['gender'],
            USER['email'],
            USER['phone'],
            USER['address'],
            USER['country']
        )
        hook.run(sql, parameters=values)



with DAG(
    dag_id = "Operation_on_postgres",
    default_args = default_args,
    description = "querying posgres using python",
    start_date = datetime.now() - timedelta(hours=1) - timedelta(minutes=2),
    schedule_interval = '*/5 * * * *'
) as dag:
    


    task1 = EmptyOperator(
        task_id="Start",
    )

    task2 = PythonOperator(
        task_id='fetch_data_task',
        python_callable=fetch_data,
        dag=dag
    )

    task3 = PythonOperator(
        task_id='insert_data_task',
        python_callable=insert_data_to_postgres,
        provide_context=True,
        dag=dag
    )

    task4 = EmptyOperator(
        task_id="End",
    )


task1 >> task2 >> task3 >> task4