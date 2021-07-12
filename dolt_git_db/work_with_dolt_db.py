import mysql.connector
import sys
import json
# import netmiko
from pprint import pprint

#Start server with "dolt sql-server" run in the folder where the repo is
#Gives an output of Starting server with Config HP="localhost:3306"|U="root"|P=""|T="28800000"|R="false"|L="info"
# Documentation here https://docs.dolthub.com/interfaces/sql/clients


ip = '192.168.0.10'
port = '3306'
db = 'test_for_dolt'
db_user = 'root'
db_password = ''
# ssh_user
# ssh_password

class dolt_work:
    def __init__(self, ip, port, db, db_user, db_password, 
    # ssh_user, ssh_password
    ):
        self.ip = ip
        self.port = port
        self.db = db
        self.db_user = db_user
        self.db_password = db_password
        # self.ssh_user = ssh_user
        # self.ssh_password = ssh_password
        # self.net_connect = netmiko.ConnectHandler(device_type="autodetect", ip=self.ip, 
        #         username=self.ssh_user, password=self.ssh_password)
        self.connection = self._connect_to_db()
        self.cursor = self.connection.cursor()

    def _connect_to_db(self):
        connection = mysql.connector.connect(
                                        user=self.db_user,
                                        host=self.ip,
                                        port=self.port,
                                        database=self.db,
                                        password = self.db_password,
                                         )
        return connection
    def run_sql_statment(self, sql_statment):
        self.cursor.execute(sql_statment)
        results = self.cursor.fetchall()
        self.connection.commit()
        return results
    def insert_to_db(self, insert_statment):
        self.cursor.execute(insert_statment)
        self.connection.commit()
    def close_conn(self):
        self.cursor.close()
        self.connection.close()
    def drop_table(self, table_name):
        self.cursor.execute(f"drop table {table_name};")
        self.connection.commit()
        return
    



test_db = dolt_work(ip, port, db, db_user, db_password)
needed_tables1 = ["bubba_joe", "json_spew"]
needed_tables2 = ["not_bubba_joe", "not_json_spew"]


def build_tables(test_db,needed_tables):
    for table in needed_tables:
        build_junk_table = f"create table {table}(json_feild text, prime_key int not null auto_increment, primary key(prime_key))"
        try:
           print(test_db.run_sql_statment(build_junk_table))
        except:
            pass

def drop_tables(test_db, needed_tables):
    for table in needed_tables:
        try:
            test_db.drop_table(table)
        except:
            pass


# drop_tables(test_db, needed_tables1)
build_tables(test_db,needed_tables1)
# build_tables(test_db,needed_tables2)
# drop_tables(test_db, needed_tables2)

print(test_db.run_sql_statment('show tables;'))



crap_data = '{"name":"John", "age":30, "car":null}'

json_data = json.loads(crap_data)



for x in range(1,3):
    json_data['age']=json_data['age']+1
    junk_json_data=json.dumps(json_data)
    insert_statment = f'''INSERT INTO bubba_joe (json_feild)VALUES ('{junk_json_data}');'''
    # print (insert_statment)
    test_db.insert_to_db(insert_statment)
select_from_table = f'select * from bubba_joe;'
try:
    pprint (test_db.run_sql_statment(select_from_table))
except:
    pass
test_db.close_conn()


# dolt sql -q "select * from json_spew"