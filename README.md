Puppy Shelter Database
========

This project sets up a puppy shelter database and demonstrates some code to manipulate that database. This repository contains the puppyShelterDBsetup.py that sets up the database, the puppypopulator.py that populates my database with shelters and puppies, and two programs that demonstrate my ability to manipulate data in this database. puppyExpressionLanguage.py uses SQLAlchemy expression language to send SQL queries to the database, and puppyORM.py which uses ORM to manipulate the database.

UPDATE: Currenly in the process of creating a webserver and web pages to view.

Technology
----------
-Python 2.7.10
-SQLite	
Special modules:
	-SQLAlchemy
-Oracle VM VirtualBox 5.0.4
-Vagrant 1.7.4

Files
-----
-ReadMe.md
-puppyExpressionLanguage.py
-puppyORM.py
-puppyShelterDBsetup.py
-puppypopulator.py

To Begin
--------
-Follow the instructions found here to install VirtualBox and Vagrant. https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true
-Install Oracle VM VirtualBox 5.0.4
-Install Vagrant 1.7.4
-Clone git repository from https://github.com/robertkohl125/PuppyShelter.git
-Navigate to fullstack/vagrant/PuppyShelter
--Files are listed above.

-From a command line run puppyShelterDBsetup.py the set up the database using
$ python puppyShelterDBsetup.py
-Then run puppypopulator.py to add puppies and shelters to the database using 
$ python puppypopulator.py
-Then open puppyORM.py or puppyExpressionLanguage.py in a text editor. Uncomment the methods and run from a command line to test my code
$ python puppyORM.py
	-or- 
$ python puppyExpressionLanguage.py

Contribute
----------
-Source Code: github.com/robertkohl125/PuppyShelter.git

Support
-------
If you are having issues, please let me know at: Robertkohl125@gmail.com
