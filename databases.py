from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, price, description, quantity,amount_of_buyers):
	product_object = Product(name=name,price =price,description = description,quantity= quantity,amount_of_buyers = amount_of_buyers)     
	session.add(product_object)
	session.commit()


create_product("bracelet", 40, "made of iron",8,442),
create_product("ring", 400, "diamond",3,42),


def update_product(name,price):
	product_object = session.query(
		Product).filter_by(
		name=name).first()
	product_object.price = price
	session.commit()


update_product("ring", 50)


def delete_product(name):
	session.query(Product).filter_by(
		name=name).delete()
	session.commit()


# delete_product("bracelet")
 

def get_product(id):
  pass
