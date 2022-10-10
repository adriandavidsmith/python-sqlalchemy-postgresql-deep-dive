import uuid
from sqlalchemy import create_engine, insert
from shared.database_service import DatabaseService
from shared.table_one import TableOne
from application import DB_URL

class SomeObject():
    def __init__(self, property_one, property_two, property_three, property_four, property_five, property_six, property_seven, property_eight):
        self.property_one = property_one
        self.property_two = property_two
        self.property_three = property_three
        self.property_four = property_four
        self.property_five = property_five
        self.property_six = property_six
        self.property_seven = property_seven
        self.property_eight = property_eight
    
    def to_dict(self):
        return {
            'property_one': self.property_one,
            'property_two': self.property_two,
            'property_three': self.property_three,
            'property_four': self.property_four,
            'property_five': self.property_five,
            'property_six': self.property_six,
            'property_seven': self.property_seven,
            'property_eight': self.property_eight
        }

def create_entries(number_of_seeds):
    entries_to_write = []
    for i in range(0, number_of_seeds):
        entry = SomeObject(
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4())
        )
        entries_to_write.append(entry)
    return entries_to_write

def to_dict(entries):
    return [i.to_dict() for i in entries]

def persist_entries(session, entries_to_write):
    session.execute(insert(TableOne.__table__), entries_to_write)

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
        dictionary_of_objects = to_dict(entries)
        persist_entries(session, dictionary_of_objects)
        query_entries(session)


if __name__ == '__main__':
    start()
