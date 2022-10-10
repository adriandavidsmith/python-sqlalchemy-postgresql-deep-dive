from sqlalchemy.orm import sessionmaker
from shared.scoped_session import ScopedSession


class DatabaseService:
    def __init__(self, engine=None):
        self.init(engine)

    def init(self, engine):
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine)

    def scoped_session(self):
        return ScopedSession(self.Session)

    def dispose_pool(self):
        self.engine.dispose()
