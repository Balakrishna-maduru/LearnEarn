from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(dag_id="Print_Date",
         start_date=datetime(2021, 1, 1),tags=["Balu","Mute"]
         ) as dag:
    print_date = BashOperator(task_id='print_date',bash_command='date')
    print_host_name = BashOperator(task_id='Get_Host_Name',bash_command='hostname')

    print_date >> print_host_name
