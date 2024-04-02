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


def querying_postgres():
    hook = PostgresHook(postgres_conn_id='postgres_localhost')
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.example_table")
    result = hook.get_records(sql="SELECT * FROM public.example_table")
    for row in result:
        print(row)
    conn.close()


with DAG(
    dag_id = "Operation_on_postgres",
    default_args = default_args,
    description = "querying posgres using python",
    start_date = datetime.now() - timedelta(hours=1) - timedelta(minutes=2),
    schedule_interval = '*/1 * * * *'
) as dag:
    


    task1 = EmptyOperator(
        task_id="Start",
    )

    task2 = EmptyOperator(
        task_id="End",
    )

    task3 = PythonOperator(
    task_id='postgres_query_task',
    python_callable=querying_postgres,
    dag=dag
    )


task1 >> task3 >> task2