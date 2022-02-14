# coding: utf-8
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Yiqing(Base):
    __tablename__ = 'yiqing'

    id = Column(INTEGER(11), primary_key=True)
    user = Column(String(255))
    password = Column(String(255))

    def to_json(self):
        return {
            'id': self.id,
            'user': self.user,
            'password': self.password
        }
