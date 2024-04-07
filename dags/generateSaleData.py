from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator


CWD = '/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/stuffs'

COMAND=f'''
record=$(python3 {CWD}/sales_details.py); \
echo $record | psql -h localhost -p 5432 -U postgres -d postgres -c "INSERT INTO public.sales  VALUES $record;"
'''


default_args = {
    'owner':"Dan4sure",
    'depends_on_past': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=10),
    'catchup': True
}


with DAG(
    dag_id = 'sales_to_db',
    default_args = default_args,
    description='A DAG to load sales into PostgreSQL',
    start_date = datetime.now() - timedelta(hours=1) - timedelta(minutes=2),
    schedule_interval = '*/5 * * * *'
) as dag:
    
    task1 = EmptyOperator(
        task_id="Start",
    )

    task2 = BashOperator(
        task_id='sales_to_db',
        bash_command=COMAND,
        dag=dag,
    )

    task3 = EmptyOperator(
        task_id="Stop",
    )


    task1 >> task2 >> task3