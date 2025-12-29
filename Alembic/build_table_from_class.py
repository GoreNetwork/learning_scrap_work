from db_connection import db_connection
from pprint import pprint
from tables import User

def populate_users_table():
    sql_insert_data_code = '''
        INSERT INTO users (telegram_id, full_name, username, language_code, referrer_id)
        VALUES
        (2001, 'Diana Prince', 'wonderwoman', 'en', NULL),
        (2002, 'Bruce Wayne', 'batman', 'en', 2001),
        (2003, 'Clark Kent', 'superman', 'en', 2001);
        '''
    db_connection.run_commit_sql_text_query(sql_insert_data_code)

def build_table_from_table_class(table_class):
    clear_users = "DROP TABLE IF EXISTS users;"
    db_connection.run_commit_sql_text_query(clear_users)
    engine = db_connection.engine
    
    #This creates the table: .create tells it to create it
    # checkfirst=True checks if the table already exists if it does do nothing otherwise create it
    # bind=engine tells it which database to create the table in
    table_class.__table__.create(bind=engine, checkfirst=True)
    populate_users_table()
    code = "select * from users;"
    result = db_connection.run_get_sql_text_query(code)
    pprint (result)


build_table_from_table_class(User)

