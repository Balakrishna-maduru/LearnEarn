from os import readlink
from azure.storage.blob import ContainerClient
import pandas as pd
import io
from io import BytesIO
output = io.StringIO()
head = ["col1" , "col2" , "col3"]
l = [[1 , 2 , 3],[4,5,6] , [8 , 7 , 9]]
df = pd.DataFrame (l , columns = head)
print(df)
output = df.to_csv(index=False)
print(output)

connection_string = "DefaultEndpointsProtocol=https;AccountName=materion2noodle;AccountKey=Qp9/dEAC+PpxX9VyqYLPqa3Wo575AD4p1Hw9ThxxtVjFpeDqhMlJWnr2JS1M8CKPwvF77hIiCU5zetIrVlLhYQ==;EndpointSuffix=core.usgovcloudapi.net;"
container_name = "noodle"
container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name=container_name)

def write(df, file, overwrite=True):
    output = df.to_csv(index=False)
    container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name=container_name)
    blob_client = container_client.upload_blob(
        name=file, data=output, overwrite=True)

write(output,'SOC2/file.txt')

def read(file):
    blob_client = container_client.get_blob_client(file)
    return blob_client.download_blob().readall()
df = pd.read_csv(BytesIO(read("SOC2/file.txt")))
print(df)