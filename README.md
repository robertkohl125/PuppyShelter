##PuppyShelter Project
========================

This project sets up a puppy shelter website supported by a database and demonstrates some code to manipulate that database. Please view my commits for latest updates.
Features include:
-All CRUD operators for database modules, 
-Flask, 
-WTForms including selects and validators, 
-Logging,
-email
-SMS (Twilio)
-Pagination on the puppies page

###Bugs/Lingering issues
------------------------
* Edit functions not auto filling HTML fields.
* Puppy picture links not working

###Technology
-------------
* Python 2.7.10
* Flask
* WTForms
* SQLite
* Bootstrap.css
* SQLAlchemy
* Oracle VM VirtualBox 5.0.4
* Vagrant 1.7.4
* Twilio

###Directory Structure
----------------------
```
+--ReadMe.md
+--config.py
+--puppyExpressionLanguage.py
+--puppyORM.py
+--puppypopulator.py
+--puppyShelterDBsetup.py
+--runserver.py
+--flask-wtf
|   +--(various WTForms files)
+--PuppyShelter
    +--__init__
    +--forms.py
    +--mainView.py
    +--models.py
    +--loginView.py
    +--ownerViews.py
    +--puppyViews.py
    +--shelterViews.py
    +--logs
    |   +--mainlog
    |   +--mainlog.log.1
    |   +--mainlog.log.3
    +--components
    |   +--__init__.py(empty file)
    |   +--script.html
    |   +--sms.py
    |   +--email.py
    +--json
    |   +--__init__.py(empty file)
    |   +--fb_client_secrets.json
    |   +--g_client_secrets.json
    |   +--gh_client_secrets.json
    +--static
    |   +--(various bootstrap.css files)
    |   +--styles.css
    |   +--stylesForm.css
    +--templates
        +--login.html
        +--adoptPuppy.html
        +--main.html
        +--ownerAll.html
        +--ownerDelete.html
        +--ownerEdit.html
        +--ownerNew.html
        +--ownerView.html
        +--puppyAll.html
        +--puppyDelete.html
        +--puppyEdit.html
        +--puppyNew.html
        +--puppyView.html
        +--shelterAll.html
        +--shelterDelete.html
        +--shelterEdit.html
        +--shelterNew.html
        +--shelterView.html
```
###To Begin
-----------
1. Follow the instructions found [here][1] to install VirtualBox and Vagrant. 
1. Follow the instructions found [here][2] to install Twilio
1. Follow the instructions found [here][3] to install Flask Mail.
1. Clone the [Github][4] repository
1. Navigate to fullstack/vagrant/PuppyShelter
--*Directory structure is listed above.
1. From a command line run runserver.py the set up the database using
--*```
$ python runserver.py
```
1. Then hit <CTRL> C to stop the process
1. Then run puppypopulator.py to add puppies and shelters to the database using 
--*```
$ python puppypopulator.py
```
1. Then run runserver.py again
--*```
$ python runserver.py
```

###Contribute
-------------
* Source Code: github.com/robertkohl125/PuppyShelter.git

###Support
----------
If you are having issues, please let me know at: Robertkohl125@gmail.com

###License
----------
The MIT License (MIT)

Copyright (c) [2015] [Robert Kohl]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[1]: https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true "Google Doc"
[2]: https://twilio-python.readthedocs.org/en/latest/ "twilio"
[3]: https://pythonhosted.org/Flask-Mail/ "Flask-Mail"
[4]: https://github.com/robertkohl125/PuppyShelter.git "Github repository"