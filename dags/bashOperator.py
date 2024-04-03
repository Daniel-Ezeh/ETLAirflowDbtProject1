from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator



PWD = '/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/stuffs/'

EXTRACTING = f'''
python3 {PWD}fetching_data.py | grep "Lagos" | cut -d "," -f2-4 | tr ")" " "  >> {PWD}weatherLog/Lag_weather.log
python3 {PWD}fetching_data.py | grep "Abuja" | cut -d "," -f2-4 | tr ")" " "  >> {PWD}weatherLog/Abj_weather.log
python3 {PWD}fetching_data.py | grep "Port Harcourt" | cut -d "," -f2-4 | tr ")" " "  >> {PWD}weatherLog/Port_weather.log
'''

BUFFERING = f'''
head -n2 < {PWD}weatherLog/Abj_weather.log > {PWD}buffered_log/Abj_weather.csv && tail -n30 <  {PWD}weatherLog/Abj_weather.log >> {PWD}buffered_log/Abj_weather.csv
head -n2 < {PWD}weatherLog/Lag_weather.log > {PWD}buffered_log/Lag_weather.csv && tail -n30 <  {PWD}weatherLog/Lag_weather.log >> {PWD}buffered_log/Lag_weather.csv
head -n2 < {PWD}weatherLog/Port_weather.log > {PWD}buffered_log/Port_weather.csv && tail -n30 <  {PWD}weatherLog/Port_weather.log >> {PWD}buffered_log/Port_weather.csv

'''

RELOADING_LOG = f'''
cat <  {PWD}buffered_log/Abj_weather.csv > {PWD}weatherLog/Abj_weather.log
cat <  {PWD}buffered_log/Lag_weather.csv > {PWD}weatherLog/Lag_weather.log
cat <  {PWD}buffered_log/Port_weather.csv > {PWD}weatherLog/Port_weather.log
'''


default_args = {
    'owner':"Dan4sure",
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'catchup': True
}


with DAG(
    dag_id = "Extraction_1.1.6",
    default_args = default_args,
    description = "this is my first dag I am writing",
    start_date = datetime.now() - timedelta(hours=1) - timedelta(minutes=2),
    # schedule_interval = timedelta(minutes=2)
    schedule_interval = '*/1 * * * *'
) as dag:
    
    task1 = EmptyOperator(
        task_id="Start",
    )

    task3 = BashOperator(
        task_id="Getting_weather_reading",
        bash_command=EXTRACTING
    )


    task4 = BashOperator(
        task_id="Buffering_weather_reading",
        bash_command=BUFFERING  
    )


    task5 = BashOperator(
        task_id="reloading_log",
        bash_command=RELOADING_LOG  
    )



task1 >> task3 >> task4 >> task5