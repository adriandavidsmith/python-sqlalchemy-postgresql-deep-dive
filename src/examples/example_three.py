import uuid
from sqlalchemy import create_engine, insert, update, bindparam
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
            str(i),
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

def update_entries(session, entries_to_write):
    table = TableOne.__table__
    update_statement = (
        update(table)
        .where(table.c.property_one == '1')
        .values(
            property_one=bindparam('property_one'),
            property_two=bindparam('property_two'),
            property_three=bindparam('property_three'),
            property_four=bindparam('property_four'),
            property_five=bindparam('property_five'),
            property_six=bindparam('property_six'),
            property_seven=bindparam('property_seven'),
            property_eight=bindparam('property_eight'),
        )
        # .returning(table.c.property_one)
    )

    result = session.execute(update_statement, entries_to_write)
    # print(result.fetchall()) error...

def start():
    database_service = DatabaseService()
    database_service.init(create_engine(DB_URL))

    with database_service.scoped_session() as session:
        session.query(TableOne).delete()
        entries = create_entries(1000)
        dictionary_of_objects = to_dict(entries)
        persist_entries(session, dictionary_of_objects)
        # update
        update_entries(session, dictionary_of_objects)


if __name__ == '__main__':
    start()
