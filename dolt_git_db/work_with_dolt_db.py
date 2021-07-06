import mysql.connector
import sys
import json
# import netmiko

#Start server with "dolt sql-server" run in the folder where the repo is
#Gives an output of Starting server with Config HP="localhost:3306"|U="root"|P=""|T="28800000"|R="false"|L="info"
# Documentation here https://docs.dolthub.com/interfaces/sql/clients


ip = '127.0.0.1'
port = '3306'
db = 'dolt'
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

try:

    # print(test_db.drop_table('json_spew'))
    print(test_db.run_sql_statment('show tables;'))
    build_table_statment= "create table json_spew(json_feild text, prime_key int not null auto_increment, primary key(prime_key))"
    build_table_statment= "create table bubba_joe(json_feild text, prime_key int not null auto_increment, primary key(prime_key))"
    print(test_db.run_sql_statment(build_table_statment))
    print(test_db.run_sql_statment('show tables;'))

except:
    pass


# build_table_statment= "drop table bubba_joe;"
print(test_db.drop_table("bubba_joe"))

crap_data = '{"name":"John", "age":30, "car":null}'

json_data = json.loads(crap_data)



for x in range(1,3):
    json_data['age']=json_data['age']+1
    junk_json_data=json.dumps(json_data)
    insert_statment = f'''INSERT INTO bubba_joe (json_feild)VALUES ('{junk_json_data}');'''
    print (insert_statment)
    test_db.insert_to_db(insert_statment)
test_db.close_conn()


# dolt sql -q "select * from json_spew"