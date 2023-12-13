Step-1: Clone the project and create a virtual environment (MUST CREATE VIRUTAL ENV)

  python -m venv myenv
  myenv\Scripts\activate

Step-2: Download the requirement.txt and the command pip install -r requirements.txt

Step-3: As this project is build on top of django. Must run the following commands to run it smoothly 
  python manage.py makemigrations
  python manage.py migrate 

  python manage.py createsuperuser (create a superuser to access the admin portal) 
  python manage.py runserver       (to start the server at port 8000) 
