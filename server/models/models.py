from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declared_attr

Base = declarative_base()

# Модель для пользователей
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    api_key = Column(String, unique=True, nullable=False)  # Уникальный API-ключ пользователя
    tweets = relationship("Tweet", back_populates="author")
    followers = relationship("User", secondary='follows',
                             primaryjoin="User.id==follows.c.followed_id",
                             secondaryjoin="User.id==follows.c.follower_id")

# Таблица подписок
follows = Table(
    'follows', Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('followed_id', Integer, ForeignKey('users.id'), primary_key=True)
)

# Модель для твитов
class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="tweets")
    likes = relationship("Like", back_populates="tweet")
    media = relationship("Media", back_populates="tweet")

# Модель для лайков
class Like(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, index=True)
    tweet_id = Column(Integer, ForeignKey('tweets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    tweet = relationship("Tweet", back_populates="likes")

# Модель для медиафайлов
class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    tweet_id = Column(Integer, ForeignKey('tweets.id'))
    tweet = relationship("Tweet", back_populates="media")
