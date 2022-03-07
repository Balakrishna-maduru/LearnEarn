import os
import sys
import json
from airflow.models import DAG
from datetime import datetime
from airflow.decorators import task
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.python_operator import PythonOperator
from airflow.operators.slack_operator import SlackAPIPostOperator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

base_path = os.getcwd()
# sys.path.append(f'{base_path}aipl/customers/materion/scripts')
# from beni_pipeline import beni_pipeline
sys.path.append("/Users/balakrishna.maduru/Documents/LearnEarn/utils")
from temp.beni_pipeline import beni_pipeline_1

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 12, 16),
}

dag = DAG('BeNi_skinny_file_Pipeline',
          default_args=default_args,
          schedule_interval=None,
          catchup=False,
          max_active_runs=1)

load_data = PythonOperator(task_id='Beni_data_loading',provide_context=True,python_callable=beni_pipeline_1,op_kwargs={"my_param":'value1'},dag=dag,)

def read_aipl_config():
    file_path = f'{base_path}/aipl/config/aipl_config.json' 
    with open(file_path) as f:
        configurations = json.load(f)
        return configurations

config = read_aipl_config()
# SLACK_CHANNEL = config['SLACK_CHANNEL']
# ALERT_PREFIX = config['ALERT_PREFIX']
# SLACK_TOKEN = config['SLACK_TOKEN']
# SLACK_USERNAME = config['SLACK_USERNAME']

send_slack_message = SlackAPIPostOperator(
    task_id='slackalert',
    token='xapp-1-A02TS2VS3S4-2932838661623-4162dffa5fc02a0335ec6582faaf7c6bf5b570181b4702bc0b6c777b88ea0994',
    channel='airflow_test_maduru',
    username='airflow',
    trigger_rule=TriggerRule.ONE_FAILED,
    text="Run of BeNi skinny file processing got failed. Please look into it ASAP.",
    dag=dag)

load_data >> send_slack_message
