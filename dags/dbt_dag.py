from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime, timedelta
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('dbt_daily_dag', default_args=default_args, schedule_interval=None)

# Define dbt tasks using BashOperator
task1 = BashOperator(
    task_id='dbt_task1',
    bash_command='dbt run --project-dir /opt/airflow/dbt/jaffle_shop --models my_first_dbt_model',
    dag=dag
)

task2 = BashOperator(
    task_id='dbt_task2',
    bash_command='dbt run --project-dir /opt/airflow/dbt/jaffle_shop --models my_second_dbt_model',
    dag=dag
)

# Set task dependencies
task1 >> task2
