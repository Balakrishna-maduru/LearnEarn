import yaml
from sqlalchemy import MetaData, Table
from data_store.database_connector import DatabaseConnector
# from database_connector import DatabaseConnector

class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def instance(self, db_details=None):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls(db_details)
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)

@Singleton
class DBConnection:

    def __init__(self, db_details):
        self.__db_details = self.__get_db_details(db_details)
        print("Establishing new data base connection")
        dc = DatabaseConnector(self.__db_details)
        self.engine = db_connection=dc.get_connection()

    def __get_db_details(self,db_details):
        if db_details is None:
            with open('config/config.yaml') as f:
                return yaml.safe_load(f).get("DB_DETAILS")
        return db_details


    def __str__(self):
        return f'Connected to db server {self.__db_details["hostname"]} and user : {self.__db_details["user"]}'

    def select(self, query):
        return self.engine.execute(query)

    def insert(self, table, data):
        metadata = MetaData()
        metadata.reflect(self.engine, only=[table])
        table = Table(table, metadata, autoload=True, autoload_with=self.engine)
        self.engine.execute(table.insert(), data)

import json
from datetime import datetime
def read_json(file):
    with open(file,'r') as file:
        return json.load(file)

if __name__ == "__main__":
    db_details = {"hostname":"192.168.1.100","user":"postgres","password":"password","port":5432,"database_name":"postgres"}
    # data = read_json("../transaction_data.json")
    # conn2 = DBConnection.instance(db_details)
    # for i in data:
    #     record = {"account_no" : i["Account No"],
    #               "transaction_date" : datetime.strptime(i["Date"], '%d %b %y'),
    #               "transaction_details" : i["Transaction Details"],
    #               "value_date" : datetime.strptime(i["Value Date"], '%d %b %y'),
    #               "withdrawal_amount" : i["Withdrawal AMT"],
    #               "deposit_amount" : i["Deposit AMT"],
    #               "balance_amount" : i["Balance AMT"] 
    #              }
    #     conn2.insert('transaction', [record])
    #     print("record : ",record)
    conn = DBConnection.instance(db_details)
    print(conn)
    for i in conn.select("select * from transaction"):
        ii = list(i)
        print(type(ii))
        print(ii)
    
    # print(conn)
    # conn2 = DBConnection.instance(db_details)
    # for i in conn2.engine.execute("select * from test"):
    #     print(i)
