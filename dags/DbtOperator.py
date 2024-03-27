# from airflow import DAG
# from dbt_airflow.operators.bash import DbtBashOperator
# from datetime import datetime

# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime(2022, 1, 1),
#     # Add any other default arguments here
# }

# with DAG(dag_id='dbt_example_dag', 
#          default_args=default_args, 
#          schedule_interval='@daily'
#          ) as dag:
    
#     dbt_run_task = DbtBashOperator(
#         task_id='dbt_run',
#         profile='my_postgres_db',
#         target='dev',
#         command='run',
#         project_dir='/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/dbt',
#         dag=dag,
#     )

