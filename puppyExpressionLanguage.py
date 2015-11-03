from sqlalchemy import *
from sqlalchemy.orm import *
from puppy_shelter_database_setup import Base, Puppy, Shelter
from sqlalchemy.sql import *
import datetime

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


#This method selects and displays all puppy names from Puppy table
def selectAllPuppies():
	s = select([Puppy])
	results = session.execute(s)
	print selectAllPuppies
	print 'selectAllPuppies:'
	print '-----------------'
	print str(s)
	for r in results:
	    print r.puppy_id, \
	    r.gender, "   ",\
	    r.name, "   ",\
	    r.weight, "lbs.   ", \
	    r.dateOfbirth, \
	    "shelter ID: ", r.shelter_id
	print 'selectAllPuppies'


#This method selects and displays all puppy names from Puppy table in alphabetical order using "select.order_by"
def selectSortAllPuppies():
	s = select([Puppy.puppy_id, Puppy.name, Puppy.gender, Puppy.dateOfbirth]).\
		order_by("puppy.name")
	results = session.execute(s)
	print 'selectSortAllPuppies:'
	print '---------------------'
	print str(s)
	for r in results:
	    print 'ID:  ', r.puppy_id, \
	    '   name:  ',r.name, \
	    '   gender:  ',r.gender, \
	    '   DOB:  ',r.dateOfbirth
	    print
	print 'selectSortAllPuppies'


#This method queries all of the puppies that are less than 6 months old organized by the youngest first.
def selectInfantPuppies():
	s = select([Puppy]).\
		where(Puppy.dateOfbirth > '2015-04-14')
	results = session.execute(s)
	print 'selectInfantPuppies:'
	print '--------------------'
	print str(s)
	for result in results:
	    print 'DOB: ', result.dateOfbirth, \
	    'Name:  ', result.name


#This method queries all puppies by ascending weight
def selectFatPuppies():
	s = select([Puppy]).\
		order_by("Puppy.weight")
	results = session.execute(s)
	print 'selectFatPuppies:'
	print '-----------------'
	print str(s)
	for result in results:
	    print 'Weight:  ',result.weight,\
	    'Name:  ',result.name


#This method queries all puppies grouped by the shelter in which they are staying
def selectPuppiesByShelter():
	j = join(Puppy, Shelter, 
		Puppy.shelter_id == Shelter.shelter_id)
	s = select([Shelter.name, Puppy.puppy_id, Puppy.name]).select_from(j).\
		order_by("shelter.name")
	results = session.execute(s).fetchall()
	print 'selectPuppiesByShelter:'
	print '-----------------------'
	print str(s)
	for r in results:
	    print r


#This method selects all data in the Shelter table and displays it.
def showShelter():
	s = select([Shelter])
	results = session.execute(s)
	print 'showShelter:'
	print '------------'
	print str(s)
	for r in results:
		print r.shelter_id, r.name
		print r.address, ", ",r.city, ", ",r.state, "   ",r.zipCode
		print r.website
		print 'maximum capacity:',r.maximum_capacity,'current_occupancy:',r.current_occupancy
		print "\n"


#selectAllPuppies()
#selectSortAllPuppies()
#selectInfantPuppies()
#selectFatPuppies()
#selectPuppiesByShelter()
#showShelter()