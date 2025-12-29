from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import atexit

class DatabaseConnection:
    def __init__(self, user, password, host, port, database):
        self.url = URL.create(
            drivername="postgresql+psycopg2",
            username=user,
            password=password,
            host=host,
            port=port,
            database=database,
        )
        print ("Database URL:", self.url)
        self.engine = create_engine(self.url
                                    # , echo=True
                                    )
        self.session_pool = sessionmaker(self.engine)
        # DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5430/postgres"
        # engine = create_engine(DATABASE_URL, echo=True)

    def run_get_sql_text_query(self, query):
        with self.session_pool() as session:
            result = session.execute(text(query))
            return result.fetchall()
        
    def run_commit_sql_text_query(self, query):
        with self.session_pool() as session:
            result = session.execute(text(query))
            session.commit()



    def close(self):
        self.engine.dispose()


db_connection = DatabaseConnection("user", "password", "127.0.0.1", 5430, "postgres")
# print (db_connection.run_get_sql_text_query("SELECT version();"))











