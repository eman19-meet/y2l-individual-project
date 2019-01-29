from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :

class User(Base):
	__tablename__ = 'users'
	user_id = Column(Integer, primary_key=True)
	uname = Column(String)
	email = Column(String)
	password = Column(String)

	def __repr__(self):
		return ("User Name: {} \n"
				"User Email : {} \n"
				"User Password: {}").format(
					self.uname,
					self.email,
					self.password)

class Posts(Base):
	__tablename__='posts'
	post_id = Column(Integer, primary_key=True)
	uname = Column(String)
	text = Column(String)
	filename = Column(String)

	def __repr__(self):
		return ("post_id: {} \n"
				"username: {} \n"
				"Post: \n"
				"		Explanaion: {} \n"
				"		Design: {} \n").format(
					self.post_id,
					self.uname,
					self.text,
					self.filename)

