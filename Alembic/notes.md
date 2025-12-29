Create the DB in docker.  This is on a PC that already has a postgres DB running, so the exposted host port is off as the real port is used.  Also the DB here won't be percistant.

```bash 
docker run --name test_postgres_db \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=postgres \
  -p 5430:5432 \
  -d postgres:13.4-alpine
  ```

  Alembinc is based on SQL Alch

  Initalize alembic with `alembic init alembic_data` with alembic_data being the folder with the alembic data

  alembic.ini is the config data for alembic.
  inside that is something that looks like `sqlalchemy.url = driver://user:pass@localhost/dbname` this is the DB URL, you don't want that as the username and password are hard coded. So we'll delete that line in alembic.ini and update the env.py (Alembic/alembic_data/env.py)

after 
```python
# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

```
we'll set the DB URL

```python
from sqlalchemy.engine import URL

def make_url(user, password, host, port, database):
    url = URL.create(
            drivername="postgresql+psycopg2",
            username=user,
            password=password,
            host=host,
            port=port,
            database=database,
        )
    return str(url)
#Rembmer that port is odd and is basically only for me to avoid issues I'm having with other local Postgres installs
# Also you'll be doing system vars for these (duh)
db_url = make_url("user", "password", "localhost", 5430, "postgres")

config.set_main_option('sqlalchemy.url', db_url)
```

Were also gonna import those tables that are in the tables.py file
```python
import os
import sys

# Get project root (directory above alembic_data)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
# This is pulling the Base.metadata which knows about all the classes inside base
from tables import Base
# Get rid of target_metadata = None
# target_metadata = None
target_metadata = Base.metadata
```

So next we'll run `alembic revision --autogenerate -m "test"` to bring the DB into alembic

```bash
(base) DT238248@DST-GJ7F9XD7J6 Alembic % alembic revision --autogenerate -m "test"
URL postgresql+psycopg2://user:password@127.0.0.1:5430/postgres
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.ddl.postgresql] Detected sequence named 'users_telegram_id_seq' as owned by integer column 'users(telegram_id)', assuming SERIAL and omitting
  Generating /Users/DT238248/Desktop/python_work/learning_scrap_work/Alembic/alembic_data/versions/ffaf046554b3_test.py ...  done
  ```
So it built `versions/ffaf046554b3_test.py` which has all the differences between what's there now, and what the difference is that that "tables" has, in this case it's adding the user table: so it built 'versions/ffaf046554b3_test.py' which has everything we need to build the users table.

We apply that change by pushing out to the head `alembic upgrade head`