from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


CWD = '/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/stuffs/'

EXTRACTING = f'''
python {CWD}fetch_customer.py | sed "s/['()]//g" >> {CWD}customer_log/customers.csv
'''


default_args = {
    'owner':"Dan4sure",
    'depends_on_past': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=10),
    'catchup': True
}


with DAG(
    dag_id = "Extracting_customer_data",
    default_args = default_args,
    description = "Extracts data",
    start_date = datetime.now() - timedelta(hours=1) - timedelta(minutes=2),
    # schedule_interval = timedelta(minutes=2)
    schedule_interval = '*/3 * * * *'
) as dag:
    
    task1 = EmptyOperator(
        task_id="Start",
    )

    task2 = BashOperator(
        task_id="Extracting_customer_data",
        bash_command=EXTRACTING  
    )

    task4 = EmptyOperator(
        task_id="Stop",
    )

    task1 >> task2 >> task4