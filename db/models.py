from sqlalchemy import (
    Column, ForeignKey, Integer, DateTime, Text, String, create_engine)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Intent(Base):
    __tablename__ = 'intent'
    __tableargs__ = {
        'comment': 'Интенты'
    }
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    text = Column(Text)


class User(Base):
    __tablename__ = 'user'
    __tableargs__ = {
        'comment': 'Пользователи'
    }
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    nickname = Column(String(64))
    name = Column(String(64))
    surname = Column(String(64))


class Message(Base):

    __tablename__ = 'message'
    __tableargs__ = {
        'comment': 'Сообщения'
    }

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    send_date = Column(DateTime)
    text = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
    bot_intent_id = Column(Integer, ForeignKey('intent.id'))
    right_intent_id = Column(Integer, ForeignKey('intent.id'))
    bot_intent = relationship('Intent', backref='message_intent',  lazy='subquery')
    right_intent = relationship('Intent', backref='message_right_intent',  lazy='subquery')
    user = relationship('User', backref='message_user',  lazy='subquery')


engine = create_engine('postgresql://postgres:liza1999@localhost:5432/med_db')
Base.metadata.create_all(engine)