1. Create app to the project: 
  - In terminal,  python manage.py startapp SimpleApps
  - In the NewProject project, open setting.py file add name_app (SimpleApp) to INSTALLED_APPS
  - Update setting for NewProject: In cmd run python manage.py migrate
2. Define URL and simple views
  - Create simple views in SimpleApp: In SimpleApp open views.py file then define home method 
  - In SimpleApp, create new urls.py file to manage SimpleApp
  - In SimpleApp, create a new URL pattern to link method home in views.py file
  - In NewProject, import include SimpleApp/urls.py on the sencond line of NewProject/urls.py
  - Working flow of url: access url: http://localhost:8000 --> NewProject/urls.py --> SimpleApp/urls --> home method
3. The structure app
  - migrations: update (add, delete, update) database schema when models change
  - admin.py: a configuration file for the built-in Django Admin app
  - apps.py: a configuration file for the app itself
  - models.py: where we define our database models which Django automatically translates into database tables
  - tests.py: test the working of the app
  - views.py: where we handle the request/response logic for our web app
  Note: __init__.py, urls.py  has the same function in NewProject but here it is in SimpleApp
4. Project and apps
  - A project represents the entire website whereas, an app is basically a submodule of the project.
  - A single project can contain multiple apps whereas, an app can also be used in different projects.
  - A project is like a blueprint of the entire web application whereas, apps are the building blocks of an web application.
  - We generally creates a single project for our website with one or more apps in it.
  - A project mantains configuration and settings realated to the whole web application. Apps on the other hand, can be independent or realted to one another.
5. About path and include function
  - Path: 
  - Include: 
  