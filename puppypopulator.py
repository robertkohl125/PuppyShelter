from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppyShelterDBsetup import Base, Shelter, Puppy, Owner
from random import randint
import datetime
import random

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#Create shelter instances
shelter1 = Shelter(
	name = "Oakland Animal Services", 
	address = "1101 29th Ave", 
	city = "Oakland", 
	state = "California", 
	zipCode = "94601", 
	website = "oaklandanimalservices.org", 
	maximum_capacity = 30)

shelter2 = Shelter(
	name = "San Francisco SPCA Mission Adoption Center", 
	address="250 Florida St", 
	city="San Francisco", 
	state="California", 
	zipCode = "94103", 
	website = "sfspca.org", 
	maximum_capacity = 35)

shelter3 = Shelter(
	name = "Wonder Dog Rescue", 
	address= "2926 16th Street", 
	city = "San Francisco", 
	state = "California" , 
	zipCode = "94103", 
	website = "http://wonderdogrescue.org", 
	maximum_capacity = 50)

shelter4 = Shelter(
	name = "Humane Society of Alameda", 
	address = "PO Box 1571", 
	city = "Alameda" , 
	state = "California", 
	zipCode = "94501", 
	website = "hsalameda.org", 
	maximum_capacity = 35)

shelter5 = Shelter(
	name = "Palo Alto Humane Society" , 
	address = "1149 Chestnut St.", 
	city = "Menlo Park", 
	state = "California" , 
	zipCode = "94025", 
	website = "paloaltohumane.org", 
	maximum_capacity = 40)

#Add all instances of shelter to the ORM
session.add_all([shelter1, shelter2, shelter3, shelter4, shelter5])

owner1 = Owner(
	firstName = "Mr. Bob" , 
	lastName = "Dobolina", 
	address = "123 North View", 
	city = "Durango", 
	state = "Colorado" , 
	zipCode = "80024", 
	cellnum = "1111111111", 
	email = "bob@dobolina.com", 
	needs = "I'm interested in getting a lovable puppy.")

owner2 = Owner(
	firstName = "Smaug" , 
	lastName = "TheTerrible", 
	address = "1 Lonely Mountain", 
	city = "Boulder", 
	state = "Colorado" , 
	zipCode = "80024", 
	cellnum = "2222222222", 
	email = "smoug@theterrible.com", 
	needs = "I want a puppy to keep me company in my mountain.")

owner3 = Owner(
	firstName = "Kylo" , 
	lastName = "Ren", 
	address = "666 Starkiller Base", 
	city = "Colorado Springs", 
	state = "Colorado" , 
	zipCode = "80024", 
	cellnum = "3333333333", 
	email = "renk@firstorder.com", 
	needs = "I need a puppy to finish what you started.")

owner4 = Owner(
	firstName = "Boba" , 
	lastName = "Fett", 
	address = "9 Jabba's Pallace", 
	city = "Mos Isley", 
	state = "Colorado" , 
	zipCode = "80024", 
	cellnum = "4444444444", 
	email = "boba@fett.com", 
	needs = "I need a hypoallergenic puppy to keep me company on long journeys.")

session.add_all([owner1, owner2, owner3, owner4])


#Add Puppies
male_names = ["Bailey", "Max", "Charlie", "Buddy", "Rocky", 
	"Jake", "Jack", "Toby", "Cody", "Buster", 
	"Duke", "Cooper", "Riley", "Harley", "Bear", 
	"Tucker", "Murphy", "Lucky", "Oliver", "Sam", 
	"Oscar", "Teddy", "Winston", "Sammy", "Rusty", 
	"Shadow", "Gizmo", "Bentley", "Zeus", "Jackson", 
	"Baxter", "Bandit", "Gus", "Samson", "Milo", 
	"Rudy", "Louie", "Hunter", "Casey", "Rocco", 
	"Sparky", "Joey", "Bruno", "Beau", "Dakota", 
	"Maximus", "Romeo", "Boomer", "Luke", "Henry"]
female_names = ['Bella', 'Lucy', 'Molly', 'Daisy', 'Maggie', 
	'Sophie', 'Sadie', 'Chloe', 'Bailey', 'Lola', 
	'Zoe', 'Abby', 'Ginger', 'Roxy', 'Gracie', 
	'Coco', 'Sasha', 'Lily', 'Angel', 'Princess', 
	'Emma', 'Annie', 'Rosie', 'Ruby', 'Lady', 
	'Missy', 'Lilly', 'Mia', 'Katie', 'Zoey', 
	'Madison', 'Stella', 'Penny', 'Belle', 'Casey', 
	'Samantha', 'Holly', 'Lexi', 'Lulu', 'Brandy', 
	'Jasmine', 'Shelby', 'Sandy', 'Roxie', 'Pepper', 
	'Heidi', 'Luna', 'Dixie', 'Honey', 'Dakota']
puppy_images = ["http://pixabay.com/get/da0c8c7e4aa09ba3a353/1433170694/dog-785193_1280.jpg?direct", 
	"http://pixabay.com/get/6540c0052781e8d21783/1433170742/dog-280332_1280.jpg?direct",
	"http://pixabay.com/get/8f62ce526ed56cd16e57/1433170768/pug-690566_1280.jpg?direct",
	"http://pixabay.com/get/be6ebb661e44f929e04e/1433170798/pet-423398_1280.jpg?direct",
	"http://pixabay.com/static/uploads/photo/2010/12/13/10/20/beagle-puppy-2681_640.jpg",
	"http://pixabay.com/get/4b1799cb4e3f03684b69/1433170894/dog-589002_1280.jpg?direct",
	"http://pixabay.com/get/3157a0395f9959b7a000/1433170921/puppy-384647_1280.jpg?direct",
	"http://pixabay.com/get/2a11ff73f38324166ac6/1433170950/puppy-742620_1280.jpg?direct",
	"http://pixabay.com/get/7dcd78e779f8110ca876/1433170979/dog-710013_1280.jpg?direct",
	"http://pixabay.com/get/31d494632fa1c64a7225/1433171005/dog-668940_1280.jpg?direct"]


#This method will make a random age for each puppy between 0-18 months(approx.) old from the day the algorithm was run.
def CreateRandomAge():
	today = datetime.date.today()
	days_old = randint(0,540)
	birthday = today - datetime.timedelta(days = days_old)
	return birthday


#This method will create a random weight between 1.0-40.0 pounds (or whatever unit of measure you prefer)
def CreateRandomWeight():
	return random.randint(1, 40)


#This method will create a random number between 1-5 for shelter ID.
def CreateRandomShelterAssignment():
	return random.randint(1, 5)


for i,x in enumerate(male_names):
	new_puppy = Puppy(name = x, 
		gender = "male", \
		dateOfbirth = CreateRandomAge(), \
		picture=random.choice(puppy_images), \
		weight= CreateRandomWeight(), \
		shelter_id = CreateRandomShelterAssignment())
	session.add(new_puppy)
	session.commit()

for i,x in enumerate(female_names):
	new_puppy = Puppy(name = x, \
		gender = "female", \
		dateOfbirth = CreateRandomAge(), \
		picture=random.choice(puppy_images), \
		weight= CreateRandomWeight(), \
		shelter_id = CreateRandomShelterAssignment())
	session.add(new_puppy)
	session.commit()