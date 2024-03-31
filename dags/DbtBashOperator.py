from pendulum import datetime
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from datetime import timedelta, datetime

PATH_TO_DBT_PROJECT = "/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/my_dbt"
PATH_TO_DBT_VENV = "/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/.venv/bin/activate"
HOME="/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1"


default_args = {
    'owner':"Dan4sure",
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'catchup': True
}

@dag(
    # schedule="@daily",
    catchup=False,
    start_date = datetime.now() - timedelta(hours=1) - timedelta(minutes=2),
    schedule_interval = '*/1 * * * *',
    default_args = default_args
)


def simple_dbt_dag():
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="export HOME=/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/my_dbt \
             && source $PATH_TO_DBT_VENV && dbt run --models .",
        env={"PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
        cwd=PATH_TO_DBT_PROJECT,
    )


simple_dbt_dag()