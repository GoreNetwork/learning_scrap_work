import mysql.connector
import sys

#Start server with "dolt sql-server" run in the folder where the repo is
#Gives an output of Starting server with Config HP="localhost:3306"|U="root"|P=""|T="28800000"|R="false"|L="info"

#Documentation here https://docs.dolthub.com/interfaces/sql/clients

def main():
    user = 'root'  # In U= above
    port = "3306"  # in HP above
    db   = 'dolt' #Folder it's in, replace - with _

    connection = mysql.connector.connect(
                                        user=user,
                                        host="127.0.0.1",
                                        port=port,
                                        database=db,
                                        password='' # In PW above
                                         )

    sql_statment = "show tables;"
    cursor = connection.cursor()
    cursor.execute(sql_statment)
    results = cursor.fetchall()
    print (results)
    cursor.close()
    connection.close()
    
    exit(0)

main()