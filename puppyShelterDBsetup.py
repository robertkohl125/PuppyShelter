from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


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
	current_occupancy = Column(Integer)


#Builds the Puppy table in the ORM
class Puppy(Base):
	"""Connects to the Puppy table
	"""
	__tablename__ = 'puppy'
	
	puppy_id = Column(Integer, primary_key = True)
	name = Column(String(10), nullable = False)
	gender = Column(String(6), nullable = False)
	dateOfbirth = Column(Integer, nullable = False)
	picture = Column(String)
	breed = Column(String)
	weight = Column(Integer, nullable = False)
	shelter_id = Column(Integer, ForeignKey('shelter.shelter_id'), nullable = False)
	shelter = relationship(Shelter, backref = "puppy")


#Builds the Puppy table in the ORM
class Owner(Base):
	"""Connects to the Owner table
	"""
	__tablename__ = 'owners'
	
	owner_id = Column(Integer, primary_key = True)
	name = Column(String(10), nullable = False)
	needs = Column(String)
	address = Column(String(30))
	city = Column(String(20))
	state = Column(String(13))
	zipCode = Column(Integer(5))
	puppy_id = Column(Integer, ForeignKey('puppy.puppy_id'))


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine) 