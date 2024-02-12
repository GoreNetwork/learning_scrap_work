from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, String, JSON, TIMESTAMP, Integer, DateTime, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def build_session():
    engine = create_engine('postgresql://dhimes:password@192.168.0.10/scrap')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


class NetworkDatasources(Base):
    __tablename__ = 'network_datasources'

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer)
    datasource_type = Column(String)
    datasource = Column(String)
    description = Column(String)
    updated = Column(DateTime)
    active = Column(Boolean)
    disabled = Column(Boolean)
    monitor_profile = Column(String)
    properties = Column(String)
