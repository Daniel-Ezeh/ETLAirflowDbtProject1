from airflow import DAG
from dbt_airflow.operators.bash import DbtBashOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.operators.empty import EmptyOperator


dbt_command = """
 dbt run --profiles-dir /Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/dbt --project-dir /Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1
 """


default_args = {
    'owner':"Dan4sure",
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'catchup': True
}


with DAG(dag_id='dbt_example_dag', 
         default_args=default_args, 
        description = "this is my first dag I am writing",
        start_date = datetime.now() - timedelta(hours=1) - timedelta(minutes=2),
        schedule_interval = '*/1 * * * *'
         ) as dag:
    

    task1 = EmptyOperator(
    task_id="Start",
    )



# Define the DBT command to run
# Run the DBT command using BashOperator
    run_dbt_task = BashOperator(
        task_id='run_dbt',
        bash_command=dbt_command
    )

task1 >> run_dbt_task