# Dataparser
A Django application that displays a list of students it employs the use of a model and CRUD operations. 
The project aims to illustrate various Django features like the MVC design pattern, SQLite and a few internal python libraries.
## Author
Caleb Bii
## Production version.
A hosted version of this application is available at https://databii.herokuapp.com/
### Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: source virtual/bin/activate
* Install all the requirements found in requirements file.
* On your terminal run python3.9 manage.py runserver
* Access the live site using the local host provided 
### Prerequisites
* python3.9  
* virtual environment
* pip 
### Clone the Repo 
* git clone https://github.com/Calebbii/Dataparser.git
* Initialize git and add the remote repository
* git init
* git remote add origin <your-repository-url>
* Create and activate the virtual environment
* python3.9-venv virtual
* source virtual/bin/activate
* Install dependancies
* Install dependancies that will create an environment for the app to run pip install -r requirements.txt
### Run The App 
* python3.9 manage.py check
* python manage.py makemigrations news
* python3.9 manage.py sqlmigrate news 0001
* python3.9 manage.py migrate
* python3.9 manage.py runserver 
* Open localhost:8000

### Testing the Application
python3.9 manager.py tests

### Built With 
* Python3.9
* Django
* Boostrap
* HTML
* CSS
### License
[MIT Lisence](https://github.com/Calebbii/Dataparser/blob/master/LICENSE) Copyright (c) 2022 Calebbii.
