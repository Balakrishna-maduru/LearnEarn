from dagster import job, op, repository
from data_profiling.data_profile import data_profile_job
# from multi_processes import my_pipeline

@repository
def noodle_data_pipelines():
    return [data_profile_job]