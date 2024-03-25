# from datetime import datetime, timedelta
# from airflow import DAG
# import airflow
# from airflow.operators.bash import BashOperator
# from airflow.operators.empty import EmptyOperator


# from datetime import datetime, timedelta
# from airflow import DAG
# import airflow
# from airflow.operators.bash import BashOperator

# default_args = {
#     'owner':"Dan4sure",
#     'retries': 5,
#     'retry_delay': timedelta(seconds=10)
# }


# with DAG(
#     dag_id = "Extraction_1",
#     default_args = default_args,
#     description = "this is my first dag I am writing",
#     start_date = datetime(2024, 2, 25, 3),
#     schedule_interval = '*/10 * * * *'
# ) as dag:
    
#     pass
#     task1 = EmptyOperator(
#         task_id="Start",
#     )

#     task2 = BashOperator(
#         task_id="bash_operator",
#         bash_command="bash /Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/stuffs/temperature_ETL.sh"
#     )

# task1 >> task2