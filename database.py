from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///databases.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def SignUp(uname, email , password ):
	user_object = User(
		uname=uname,
		email=email,
		password=password)
	session.add(user_object)
	session.commit()

def query_by_name(uname):
	user = session.query(User).filter_by(
		uname=uname).first()
	print(user)
	return user.uname

def query_by_pass(uname):
	user = session.query(User).filter_by(
		uname=uname).first()
	print(user)
	return user.password

def query_all():
	users = session.query(User).all()
	return users

def query_by_id(user_id):
    user = session.query(User).filter_by(
        user_id=user_id).first()
    return user


def add_post(uname, text , filename):
	post_object = Posts(
		uname=uname,
		text=text,
		filename=filename)
	session.add(post_object)
	session.commit()

def query_all_posts():
	"""
	Print all the posts in the database.
	"""
	p = session.query(Posts).all()
	posts = []
	posts=p
	return posts



