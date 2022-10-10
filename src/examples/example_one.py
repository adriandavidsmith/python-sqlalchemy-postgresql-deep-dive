import uuid
from sqlalchemy import create_engine
from shared.database_service import DatabaseService
from shared.table_one import TableOne
from application import DB_URL

# @profile
def persist_entries(session, entries_to_write):
    for entry in entries_to_write:
        session.add(entry)
    session.commit()

# @profile
def create_entries(number_of_seeds):
    entries_to_write = []
    for i in range(0, number_of_seeds):
        entry = TableOne()
        entry.property_one = str(uuid.uuid4())
        entry.property_two = str(uuid.uuid4())
        entry.property_three = str(uuid.uuid4())
        entry.property_four = str(uuid.uuid4())
        entry.property_five = str(uuid.uuid4())
        entry.property_six = str(uuid.uuid4())
        entry.property_seven = str(uuid.uuid4())
        entry.property_eight = str(uuid.uuid4())
        entries_to_write.append(entry)
    return entries_to_write

# @profile
def query_entries(session):
    entries = session.query(TableOne).all()
    print(len(entries))


@profile
def start():
    database_service = DatabaseService()
    database_service.init(create_engine(DB_URL))

    with database_service.scoped_session() as session:
        session.query(TableOne).delete()
        entries = create_entries(100000)
        persist_entries(session, entries)
        query_entries(session)


if __name__ == '__main__':
    start()
