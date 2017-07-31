from sqlalchemy import Column, Text, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Notes(Base):
    __tablename__ = "notes"
    chat_id = Column(String(14), primary_key=True)
    name = Column(Text, primary_key=True)
    value = Column(Text, nullable=False)

    def __init__(self, chat_id, name, value):
        self.chat_id = chat_id
        self.name = name
        self.value = value

    def __repr__(self):
        return "<Note %s>" % self.name
