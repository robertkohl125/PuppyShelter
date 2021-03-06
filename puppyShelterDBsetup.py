from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import logging


Base = declarative_base()


logging.info('puppyShelterDBSetup.py file accessed')


#Builds the Shelter table in the ORM
class Shelter(Base):
	"""Connects to the Shelter table
	"""
	__tablename__ = 'shelter'
	
	shelter_id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	address = Column(String(30))
	city = Column(String(20))
	state = Column(String(13))
	zipCode = Column(Integer(5))
	website = Column(String)
	maximum_capacity = Column(Integer, nullable = False)
	current_occupancy = Column(Integer, default = 0)
	remaining_spaces = Column(Integer)


#Builds the Owner table in the ORM
class Owner(Base):
	"""Connects to the Owner table
	"""
	__tablename__ = 'owner'
	
	owner_id = Column(Integer, primary_key = True)
	firstName = Column(String(15), nullable = False)
	lastName = Column(String(30), nullable = False)
	address = Column(String(30))
	city = Column(String(20))
	state = Column(String(13))
	zipCode = Column(Integer(5))
	cellnum = Column(Integer(10))
	email = Column(String)
	needs = Column(String)
	authenticated = Column(Boolean, default = False)
	active = Column(Boolean, default = False)
	anonymous = Column(Boolean, default = False)




#Builds the Puppy table in the ORM
class Puppy(Base):
	"""Connects to the Puppy table
	"""
	__tablename__ = 'puppy'
	
	puppy_id = Column(Integer, primary_key = True)
	name = Column(String(10), nullable = False)
	gender = Column(String(6), nullable = False)
	dateOfbirth = Column(Date, nullable = False)
	picture = Column(String)
	breed = Column(String, default = 'Unknown')
	weight = Column(Integer, nullable = False)
	shelter_id = Column(Integer, ForeignKey('shelter.shelter_id'))
	shelter = relationship(Shelter, backref = 'puppy')
	owner_id = Column(Integer, ForeignKey('owner.owner_id'))
	owner = relationship(Owner, backref = 'puppy')


class User(Base):
	"""Connects to the User table
	"""
	__tablename__ = 'user'
	
	user_id = Column(Integer, primary_key = True)
	name = Column(String(30), nullable = False)
	address = Column(String(30))
	city = Column(String(20))
	state = Column(String(13))
	zipCode = Column(Integer(5))
	cellnum = Column(Integer(10))
	picture = Column(String)
	email = Column(String, nullable = False)
	is_authenticated = Column(String)



engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine) 