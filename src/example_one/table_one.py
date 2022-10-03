from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TableOne(Base):
    __tablename__ = 'table_one'
    
    id = Column(Integer, primary_key=True)
    property_one = Column(String, nullable=False)
    property_two = Column(String, nullable=False)
    property_three = Column(String, nullable=False)
    property_four = Column(String, nullable=False)
    property_five = Column(String, nullable=False)
    property_six = Column(String, nullable=False)
    property_seven = Column(String, nullable=False)
    property_eight = Column(String, nullable=False)
