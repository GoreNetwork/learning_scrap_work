from db_connection import db_connection
from pprint import pprint
from tables import User

clear_users = "DROP TABLE IF EXISTS users;"

def build_populate_drop_table_from_sql_query():
    sql_make_table_code = '''CREATE TABLE users (
        telegram_id   BIGINT PRIMARY KEY,
        full_name     TEXT NOT NULL,
        username      TEXT,
        language_code TEXT NOT NULL,
        created_at    TIMESTAMP DEFAULT now(),
        referrer_id   BIGINT,
        CONSTRAINT fk_users_referrer
            FOREIGN KEY (referrer_id)
            REFERENCES users (telegram_id)
            ON DELETE SET NULL
            );'''
    sql_insert_data_code = '''
            INSERT INTO users (telegram_id, full_name, username, language_code, referrer_id)
            VALUES
            (2001, 'Diana Prince', 'wonderwoman', 'en', NULL),
            (2002, 'Bruce Wayne', 'batman', 'en', 2001),
            (2003, 'Clark Kent', 'superman', 'en', 2001);
            '''
    code_to_commit = [clear_users, sql_make_table_code, sql_insert_data_code]

    for code in code_to_commit:
        db_connection.run_commit_sql_text_query(code)

    code = "select * from users;"
    result = db_connection.run_get_sql_text_query(code)
    pprint (result)
    result = db_connection.run_commit_sql_text_query(clear_users)
    pprint (result) 

# build_populate_drop_table_from_sql_query()

db_connection.run_commit_sql_text_query(clear_users)


