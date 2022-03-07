import yaml
import numpy as np
from datetime import datetime
from data_store.data_reader import ReadWriter
from dagster import job, op, get_dagster_logger, solid
from data_profiling.report_generator import ReportGenerator


def processes_files(context, html_output_dir, files):
    rw = ReadWriter()
    rg = ReportGenerator()
    for file in files:
        get_dagster_logger().info(f"Started report generation for file : {file}")
        df = rw.read_csv(file)
        rg.generate(df, html_output_dir, file)

def read_bucket():
    with open('config/config.yaml') as f:
        return yaml.safe_load(f).get("BUCKET_SIZE",1)

@op
def get_matadate(context):
    rw = ReadWriter()
    file_path=context.op_config["file_path"]
    html_output_dir=context.op_config["html_output_dir"]
    get_dagster_logger().info("Started metadata extraction")
    files = rw.get_filepaths(file_path)
    return html_output_dir, np.array_split(files, read_bucket())

def profile(value):
    @solid(
        name=f"_data_profling_{value}",
        tags={
            "value": f"{value}",
        },
    )
    def _profile(context, metadata):
        index = context.solid_def.tags['value']
        data_files = metadata[1][int(index)]
        html_output_dir = metadata[0]
        processes_files(context, html_output_dir, data_files)
    return _profile

@job
def data_profile_job():
    metadata = get_matadate()
    for i in range(read_bucket()):
        profile(i)(metadata)

# if __name__ == "__main__":
#     result = data_profile_job.execute_in_process()