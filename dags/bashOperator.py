from datetime import datetime, timedelta
from airflow import DAG
import airflow
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta
from airflow import DAG
import airflow
from airflow.operators.bash import BashOperator

default_args = {
    'owner':"Dan4sure",
    'retries': 5,
    'retry_delay': timedelta(seconds=10)
}


with DAG(
    dag_id = "my_first_dag_v4.1.1",
    default_args = default_args,
    description = "this is my first dag I am writing",
    start_date = datetime(2024, 2, 25, 3),
    schedule_interval = '*/10 * * * *'
) as dag:
    task1 = BashOperator(
        task_id="bash_operator",
        bash_command="echo hello world, this is the first task!"
    )