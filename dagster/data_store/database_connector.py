from enum import Enum
import sqlalchemy as db

class DatabaseConnectConstant(Enum):
    USER = "user"
    PASSWORD = "password"
    PORT = "port"
    HOSTNAME = "hostname"
    DATABASE_NAME = 'database_name'
    DATABASE_TYPE = "database_type"

class DatabaseConnector:

    def __init__(self, db_details, database_type='postgresql') -> None:
        self.database_type = database_type
        self.user = db_details.get(DatabaseConnectConstant.USER.value)
        self.password = db_details.get(DatabaseConnectConstant.PASSWORD.value)
        self.port = db_details.get(DatabaseConnectConstant.PORT.value)
        self.hostname = db_details.get(DatabaseConnectConstant.HOSTNAME.value)
        self.database_name = db_details.get(DatabaseConnectConstant.DATABASE_NAME.value,False)

    def get_connection(self) -> str:
        connection_string = f'{self.database_type}://{self.user}:{self.password}@{self.hostname}:{self.port}'
        if self.database_name:
            connection_string = f'{self.database_type}://{self.user}:{self.password}@{self.hostname}:{self.port}/{self.database_name}'
        return db.create_engine(connection_string).connect()