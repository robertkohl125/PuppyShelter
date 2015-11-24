from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SelectField, validators
from wtforms.fields import TextField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required, InputRequired
from wtforms.widgets import Select


class SelectWithRedFrame(Select):
    def __init__(self, error_class=u'has_errors'):
        super(SelectWithRedFrame, self).__init__()
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        if field.errors:
            c = kwargs.pop('class', '') or kwargs.pop('class_', '')
            kwargs['class'] = u'%s %s' % (self.error_class, c)
        return super(SelectWithRedFrame, self).__call__(field, **kwargs)


class ShelterForm(Form):
	"""Sets definitions and validators for Shelter forms"""

	name = StringField('Name', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=50, 
    		message="Limit 50 characters, please try again.")])
	address = StringField('Address', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=30, 
    		message="Limit 30 characters, please try again.")])
	city = StringField('City', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=20, 
    		message="Limit 20 characters, please try again.")])
	state = StringField('State', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=13, 
    		message="Limit 13 characters, please try again.")])
	zipCode = IntegerField('zipCode', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=10, 
    		message="xxxxx or xxxxx-xxxx")])
	website = StringField('Website', 
    	[validators.InputRequired(),
    	validators.URL(
    		message="Not a valid URL")])
	maximum_capacity = IntegerField('maximum_capacity', 
    	[validators.InputRequired()])


class PuppyForm(Form):
	"""Sets definitions and validators for Puppy forms"""

	name = StringField('Name', 
    	[validators.InputRequired(),
    	validators.Length(
    		max=10, 
    		message="Limit 10 characters.")])
	gender = SelectField('Gender', 
    	choices=[('male', 'male'), ('female', 'female')])
	dateOfBirth = DateField("Date of Birth", 
    	[validators.InputRequired()])
	picture = StringField('Picture', 
    	[validators.InputRequired()])
	breed = StringField('Breed', 
    	[validators.InputRequired()])
	weight = IntegerField('Weight', 
    	[validators.InputRequired(), 
    	validators.NumberRange(
    		min=1, max=1000, 
    		message="Between 1 and 1000.")])
	shelter_id = IntegerField('Weight', 
    	[validators.InputRequired(), 
    	validators.NumberRange(
    		min=1, max=10, 
    		message="Please choose a shelter.")])


class OwnerForm(Form):
	"""Sets definitions and validators for Owner forms"""

	firstName = StringField('First Name', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=15, 
    		message="Limit 15 characters.")])
	lastName = StringField('Last Name', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=30, 
    		message="Limit 30 characters.")])
	address = StringField('Address', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=30, 
    		message="Limit 30 characters.")])
	city = StringField('City', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=20, 
    		message="Limit 20 characters.")])
	state = StringField('State', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=13, 
    		message="Limit 13 characters.")])
	zipCode = IntegerField('zipCode', 
    	[validators.InputRequired(), 
    	validators.Length(
    		max=10, 
    		message="xxxxx or xxxxx-xxxx")])
	email = TextField(('Email'),
    	[validators.InputRequired(message=('Email is required')),
    	validators.Email(message=('Please enter a valid email'))])
	needs = TextAreaField('Needs', 
    	[validators.InputRequired()])


class AdoptionForm(Form):
	owner_id = IntegerField('Owner', 
		[validators.InputRequired(), 
		validators.Length(
			max=80, 
			message="Choose a human candidate for this adoption.")])

