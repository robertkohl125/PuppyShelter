Puppy Shelter Database
========

This project sets up a puppy shelter website supported by a database and demonstrates some code to manipulate that database. Please view my commits for latest updates.
Features include:
-All CRUD operators for database modules, 
-Flask, 
-WTForms including selects and validators, 
-Logging,
-email
-SMS

!!BugsLingering issues!!
----------------
*logging not working within methods: TypeError: 'unicode' object is not callable.
*Edit functions not completely updated to WTForms and not auto filling fields in.
*Pagination not working.
*email server not live.
*sms not functional yet.

Technology
----------
-Python 2.7.10
-Flask
-WTForms
-SQLite
-Bootstrap.css
-SQLAlchemy
-Oracle VM VirtualBox 5.0.4
-Vagrant 1.7.4

Files
-----
/ReadMe.md
/config.py
/puppyExpressionLanguage.py
/puppyORM.py
/puppypopulator.py
/puppyShelterDBsetup.py
/runserver.py
/flask-wtf
	/(various WTForms files)
/PuppyShelter
	/__init__
	/forms.py
	/mainView.py
	/models.py
	/ownerViews.py
	/puppyViews.py
	/shelterViews.py
	/static
		/(various bootstrap.css files)
		/styles.css
		/stylesForm.css
	/templates
		/adoptPuppy.html
		/main.html
		/ownerAll.html
		/ownerDelete.html
		/ownerEdit.html
		/ownerNew.html
		/ownerView.html
		/puppyAll.html
		/puppyDelete.html
		/puppyEdit.html
		/puppyNew.html
		/puppyView.html
		/shelterAll.html
		/shelterDelete.html
		/shelterEdit.html
		/shelterNew.html
		/shelterView.html

To Begin
--------
-Follow the instructions found here to install VirtualBox and Vagrant. https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true
-Install Oracle VM VirtualBox 5.0.4
-Install Vagrant 1.7.4
-Clone git repository from https://github.com/robertkohl125/PuppyShelter.git
-Navigate to fullstack/vagrant/PuppyShelter
--Files are listed above.

-From a command line run runserver.py the set up the database using
$ python runserver.py 
-Then hit <CTRL> C to stop the process
-Then run puppypopulator.py to add puppies and shelters to the database using 
$ python puppypopulator.py
-Then run runserver.py again
$ python runserver.py 

Contribute
----------
-Source Code: github.com/robertkohl125/PuppyShelter.git

Support
-------
If you are having issues, please let me know at: Robertkohl125@gmail.com
