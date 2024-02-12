from datetime import datetime, timedelta
from db_conn_table_data import build_session, NetworkDatasources
from sqlalchemy import update




def update_devices_by_id(ids_to_update):
    now = datetime.now()
    test = update(NetworkDatasources).where(NetworkDatasources.id.in_(ids_to_update)).values(updated=now)
    session.execute(test)
    # commit the changes
    session.commit()

session = build_session()
ids_to_update = [3,5]
update_devices_by_id(ids_to_update)

def add_device():
    # Create a new VersaAppliance object with the same attributes as the device
    new_device = NetworkDatasources(
        device_id = 666,
        datasource_type = 'interface',
        datasource = 'test',
        description = 'bubba',
        updated = 'ted',
        active = True,
        disabled = False,
        monitor_profile = "bubba",
        properties = "{}",
    )

    # Merge the new_device object with the corresponding row in the database
    session.merge(new_device)

    # Commit the changes to the database
    session.commit()

add_device()