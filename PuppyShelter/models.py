from sqlalchemy import *
from sqlalchemy.orm import *
from puppyShelterDBsetup import Base, Puppy, Shelter, Owner
from sqlalchemy.sql import *
import datetime
import logging


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


#This method selects and displays all puppy names from Puppy table
def adoptPuppy(puppy_id, ownr, shelt):
	puppy = selectAllPuppies().filter_by(puppy_id=puppy_id)
	o = selectAllOwners().filter_by(owner_id=ownr)
	if o is None:
		owner = "No owners available, must create an owner profile"
	else:
		for p in puppy:
			p.shelter_id = None
			p.owner_id = ownr


def selectAllPuppies():
	logging.info('**models.selectAllPuppies called')
	puppies = session.query(Puppy)
	return puppies


def selectAllShelters():
	logging.info('**models.selectAllShelters called')
	updateCurrentOccupancy()
	shelters = session.query(Shelter)
	return shelters


def selectAllOwners():
	logging.info('**models.selectAllOwners called')
	owners = session.query(Owner)
	return owners


def createPuppy(new_puppy):
	newPuppy = Puppy(
    	name = new_puppy['name'],
		gender = new_puppy['gender'],
		dateOfbirth = new_puppy['dateOfbirth'],
		picture = new_puppy['picture'],
		breed = new_puppy['breed'],
		weight = new_puppy['weight'],
		shelter_id = new_puppy['shelter_id'])
	session.add(newPuppy)
	session.commit()


def createShelter(new_shelter):
	newShelter = Shelter(
		name = new_shelter['name'],
		address = new_shelter['address'],
		city = new_shelter['city'],
		state = new_shelter['state'],
		zipCode = new_shelter['zipCode'],
		website = new_shelter['website'],
		maximum_capacity = new_shelter['maximum_capacity'],
		current_occupancy = 0)
	session.add(newShelter)
	session.commit()


def createOwner(new_owner):
	newOwner = Owner(
    	firstName = new_owner['firstName'],
    	lastName = new_owner['lastName'],
		address = new_owner['address'],
		city = new_owner['city'],
		state = new_owner['state'],
		zipCode = new_owner['zipCode'],
		email = new_owner['email'],
		needs = new_owner['needs'])
	session.add(newOwner)
	session.commit()


#
def deletePuppy(puppy_id):
	delPuppy = session.query(Puppy).filter_by(puppy_id=puppy_id)
	for d in delPuppy:
		deleteItem = Puppy(puppy_id=puppy_id)
	session.delete(d)
	session.commit()


#
def deleteShelter(shelter_id):
	delShelter = session.query(Shelter).filter_by(shelter_id=shelter_id)
	for d in delShelter:
		deleteItem = Shelter(shelter_id=shelter_id)
	session.delete(d)
	session.commit()


#
def deleteOwner(owner_id):
	delOwner = session.query(Owner).filter_by(owner_id=owner_id)
	for d in delOwner:
		deleteItem = Owner(owner_id=owner_id)
	session.delete(d)
	session.commit()


def editPuppy(edit_puppy, puppy_id):
	puppy = session.query(Puppy).filter_by(puppy_id=puppy_id)
	editPup = Puppy(
		name = edit_puppy['name'],
		gender = edit_puppy['gender'],
		dateOfbirth = edit_puppy['dateOfbirth'],
		picture = edit_puppy['picture'],
		breed = edit_puppy['breed'],
		weight = edit_puppy['weight'],
		shelter_id = edit_puppy['shelter_id'])
	for p in puppy:
		p.name = editPup.name
		p.gender = editPup.gender
		p.dateOfbirth = editPup.dateOfbirth
		p.picture = editPup.picture
		p.breed = editPup.breed
		p.weight = editPup.weight
 		p.shelter_id = editPup.shelter_id	
	session.add(p)
	session.commit
	


def editShelter(edit_shelter, shelter_id):
	shelter = session.query(Shelter).filter_by(shelter_id=shelter_id)
	editShelt = Shelter(
		name = edit_shelter['name'],
		address = edit_shelter['address'],
		city = edit_shelter['city'],
		state = edit_shelter['state'],
		zipCode = edit_shelter['zipCode'],
		website = edit_shelter['website'],
		maximum_capacity = edit_shelter['maximum_capacity'])
	for s in shelter:
		s.name = editShelt.name
		s.address = editShelt.address
		s.city = editShelt.city
		s.state = editShelt.state
		s.zipCode = editShelt.zipCode
		s.website = editShelt.website
 		s.maximum_capacity = editShelt.maximum_capacity	
	session.add(s)
	session.commit


def editOwner(edit_owner, owner_id):
	owner = session.query(Owner).filter_by(owner_id=owner_id)
	editOwn = Owner(
    	firstName = edit_owner['firstName'],
    	lastName = edit_owner['lastName'],
		address = edit_owner['address'],
		city = edit_owner['city'],
		state = edit_owner['state'],
		zipCode = edit_owner['zipCode'],
		email = edit_owner['email'],
		needs = edit_owner['needs'])
	for o in owner:
		o.firstName = editOwn.firstName
		o.lastName = editOwn.lastName
		o.address = editOwn.address
		o.city = editOwn.city
		o.state = editOwn.state
		o.zipCode = editOwn.zipCode
		o.email = editOwn.email
		o.needs = editOwn.needs
	session.add(o)
	session.commit


def selectPuppy(puppy_id):
	puppies = session.query(Puppy).filter_by(puppy_id=puppy_id)
	return puppies


def selectShelter(shelter_id):
	updateCurrentOccupancy()
	shelters = session.query(Shelter).filter_by(shelter_id=shelter_id)
	return shelters


def selectOwner(owner_id):
	owners = session.query(Owner).filter_by(owner_id=owner_id)
	return owners


def selectEnrolledShelter(puppy_id):
	updateCurrentOccupancy()
	puppy = selectAllPuppies().filter_by(puppy_id=puppy_id)
	for p in puppy:
		shelt = p.shelter_id
	shelter = session.query(Shelter).filter_by(shelter_id=shelt)
	return shelter


def selectAdopterOwners(puppy_id):
	powner = session.query(Puppy).filter_by(puppy_id=puppy_id)
	for o in powner:
		owner_id = o.owner_id
	owner = session.query(Owner).filter_by(owner_id=owner_id)
	return owner


def selectOwnerWOPuppies():
	owners = session.query(Owner).filter_by(puppy_id=None)
	return owners


def selectAvailableShelters():
	updateCurrentOccupancy()
	shelters = session.query(Shelter).filter(Shelter.remaining_spaces > 1).order_by(asc(Shelter.remaining_spaces))
	return shelters


#This method selects and displays all puppy names from Puppy table in alphabetical order.
def selectSortAllPuppies():
	s = session.query(Puppy.puppy_id, Puppy.name, Puppy.gender, Puppy.dateOfbirth).\
		order_by("puppy.name")
	results = session.execute(s)
	print 'selectSortAllPuppies:'
	print '---------------------'
	print str(s)
	for r in results:
	    print r[1], r #puppy.name(results tuple)
	print 'selectSortAllPuppies'


#This method queries all of the puppies that are less than 6 months old (born after 2015-04-14) organized by the youngest first.
def selectInfantPuppies():
	s = session.query(Puppy.name, Puppy.dateOfbirth).\
		filter(Puppy.dateOfbirth > '2015-04-14').\
		order_by(desc(Puppy.dateOfbirth))
	results = session.execute(s)
	print 'selectInfantPuppies:'
	print '--------------------'
	print str(s)
	for r in results:
	    print r[0], r[1]


#This method queries all puppies by ascending weight
def selectFatPuppies():
	s = session.query(Puppy.name, Puppy.weight).\
		order_by(Puppy.weight)
	s.all() #returns query results as list
	results = session.execute(s)


#This method queries all puppies grouped by the shelter in which they are staying
def selectPuppiesByShelter(shelter_id):
	puppies = session.query(Puppy).filter_by(shelter_id=shelter_id)
#	o = puppies.order_by("shelter.shelter_id") #add the order_by method
	return puppies


#This method counts all puppies by the shelter in which they are staying.
def countCurrentOccupancy():
	p = session.query(Puppy.shelter_id, func.count(Puppy.shelter_id))
	p_grouped_count = p.group_by (Puppy.shelter_id)
	return p_grouped_count


#This method returns current_occupancy from the Shelter table as a list of only current_occupancy values
def countUpdatedOccupancy():
	p = session.query(Shelter.shelter_id, Shelter.current_occupancy)
	w = []
	for row in p:
		w.append(row[1])
	return w


#This method updates Shelter.current_occupancy with the countCurrentOccupancy().
def updateCurrentOccupancy():
	counts_list = countCurrentOccupancy()
	counts_dict = dict(counts_list)
	shelters = session.query(Shelter)
	for shelter in shelters:
		shelter.current_occupancy = counts_dict.get(shelter.shelter_id)
		if shelter.current_occupancy is None:
			co = 0
		else:
			co = shelter.current_occupancy
		shelter.remaining_spaces = shelter.maximum_capacity - co
		session.add(shelter)
	session.commit()


#This method tests for overall capacity and calls the createShelterPuppyRow() method if there is availability.
def testAvailability():
	updateCurrentOccupancy()
	t = calcCurrentOccDiff()
	total = sum(t)
	print total
	if total < 0:
		print 'Shelters beyond capacity, please open a new shelter.'
	else:
		createShelterPuppyRow()


#This method inserts a new dog into the db and finds the best shelter for it.
def findLowestOccupancyShelter():
	count = countUpdatedOccupancy()
	min_count = min(count)

	s = session.query(Shelter.shelter_id).\
		filter(Shelter.current_occupancy == min_count).\
		first()

	print 'findLowestOccupancyShelter:'
	print '---------------------------'
	print min_count
	for row in s:
		print row
	print type(s)
	print 'shelter with lowest occupancy:', s[0]
	return s[0] #returns first in the list


#This method calculates the available spaces and returns these values as a list
def calcCurrentOccDiff():
	mc = session.query(Shelter.shelter_id, Shelter.maximum_capacity)
	co = session.query(Shelter.shelter_id, Shelter.current_occupancy)
	print 'calcCurrentOccDiff:'
	print '-------------------'
	print 'SQL: ', str(co) #prints the SQL query
	print 'SQL: ', str(mc) #prints the SQL query
	for row in co:
		print row
	for row in mc:
		print row

	dict_mc = dict(mc) #translates results into a dictionary
	dict_co = dict(co) #translates results into a dictionary
	dict_calc = {key: dict_mc[key] - dict_co.get(key, 0) for key in dict_mc.keys()} #calculates the difference between dictionary values
	list_calc = list(dict_calc.values())
	print list_calc
	return list_calc

