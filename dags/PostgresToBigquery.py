from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator, BigQueryUpdateDatasetOperator
from datetime import timedelta, datetime
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator


default_args = {
    'owner':"Dan4sure",
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'catchup': True
}


with DAG(
    dag_id='Migration',
    description='A DAG to load data from PostgreSQL to BigQuery',
    tags=['really'],
    catchup=False,
    start_date = datetime.now() - timedelta(hours=1) - timedelta(minutes=2),
    schedule_interval = '*/1 * * * *',
    default_args = default_args
) as dag:


    start = EmptyOperator(
        task_id='start'
    )

    end = EmptyOperator(
        task_id='end'
    )


    extract_from_postgres = PostgresOperator(
        task_id='extract_from_postgres',
        sql='SELECT * FROM public.example_table ;',
        postgres_conn_id='postgres_default',
        dag=dag,
    )

    # load_to_bigquery = BigQueryOperator(
    #     task_id='load_to_bigquery',
    #     sql='SELECT * FROM your_table;',
    #     destination_dataset_table='your_project.your_dataset.your_table',
    #     write_disposition='WRITE_TRUNCATE',
    #     bigquery_conn_id='google_cloud_default',
    #     use_legacy_sql=False,
    #     dag=dag,
    # )



    create_new_dataset = BigQueryCreateEmptyDatasetOperator(
        dataset_id='from_postgres',
        project_id='ETL-dbt-bigquery',
        dataset_reference={"friendlyName": "New Dataset"},
        gcp_conn_id='_my_gcp_conn_',
        task_id='newDatasetCreator',
        dag=dag,
    )

start >> extract_from_postgres >> create_new_dataset >> end