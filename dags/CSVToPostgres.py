from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator



FILE_PATH = '/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/stuffs/customer_log/'

COMMAND='''
FILE_PATH=/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/stuffs/customer_log ; \
header=$(head -n 1 $FILE_PATH/customers.csv) ;
echo "$header" > $FILE_PATH/customers.csv
'''


default_args = {
    'owner':"Dan4sure",
    'depends_on_past': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=10),
    'catchup': True
}


with DAG(
    dag_id = 'load_csv_to_postgres',
    default_args = default_args,
    description='A DAG to load a CSV file into PostgreSQL',
    start_date = datetime.now() - timedelta(hours=1) - timedelta(minutes=2),
    # schedule_interval = timedelta(minutes=2)
    schedule_interval = '*/30 * * * *'
) as dag:
    
    task1 = EmptyOperator(
        task_id="Start",
    )

    task2 = PostgresOperator(
        task_id='load_csv_to_postgres',
        postgres_conn_id='postgres_localhost',  # Name of your PostgreSQL connection
        sql=f'COPY customers FROM \'{FILE_PATH}customers.csv\' DELIMITER \',\' CSV HEADER;',
        dag=dag,
    )


    task3 = BashOperator(
        task_id="Truncating_record_from_csv_file",
        bash_command=COMMAND  
    )
    task4 = EmptyOperator(
        task_id="Stop",
    )



    task1 >> task2 >> task3 >> task4