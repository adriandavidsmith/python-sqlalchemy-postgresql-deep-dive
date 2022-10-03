from sqlalchemy import create_engine
from shared.database_service import DatabaseService
from application import DB_URL
from example_one.table_one import TableOne

if __name__ == '__main__':
    database_service = DatabaseService()
    database_service.init(create_engine(DB_URL))

    with database_service.scoped_session() as session:
        entries = session.query(TableOne).all()
        print(entries)
