from azure.storage.blob import ContainerClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=materion2noodle;AccountKey=Qp9/dEAC+PpxX9VyqYLPqa3Wo575AD4p1Hw9ThxxtVjFpeDqhMlJWnr2JS1M8CKPwvF77hIiCU5zetIrVlLhYQ==;EndpointSuffix=core.usgovcloudapi.net;"
container_name = "incremental-data"

container = ContainerClient.from_connection_string(conn_str=connection_string, container_name=container_name)

blob_list = container.list_blobs()
for blob in blob_list:
    print(blob.name + '\n')