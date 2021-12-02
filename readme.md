# Instruction
1. What is Django?
>>>
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
>>>
2. Django MTV pattern
  - MTV: Model-Template-View
  - Model (M): Logical data structure
  - Template (T): Presentation layer
  - View (V): Data formatting
  - Working flow of Django framework: Template --> View --> Models --> View --> Template
**Require**: Let user Python3
## Install django 
  ```shell script
      pip install Django
  ```

# 1. Start new project
### Create a project
  ```shell script
      django-admin startproject NewProject
  ```
<p>This will create a NewProject directory in your current directory</p>

> *Note: *Name_project avoid using name like "Django" or "Test"
<p>Structure a project</p>

```shell script
NewProject/
    manage.py
    NewProject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

<p>These files are:</p>
  - manage.py: used as a command-line utility for our projects (use for debugging, deploying and runing our web applications)
  - __init__.py: the Python interpreter
  - asgi.py: (Asynchronours server gateway interface) the same wsgi
  - setting.py: project configuration
  - urls.py: URLs of web pages to link web pages together
  - wsgi.py: (web server gateway interface)deploy project to server
  
#### Run server:
 - Run with port default: `python manage.py runserver`
 - Run with port 8080: `python manage.py runserver 8080`

# 2. Create a new app + URLs Mapping + Simple View
### Create a new app
  - In `...\NewProject>`,  `python manage.py startapp SimpleApps`
  - In the NewProject project, open setting.py file add name_app (SimpleApp) to INSTALLED_APPS
  - Update setting for NewProject: In `...\NewProject>`: `python manage.py migrate`
### Define URL + simple views
  - Create simple views in SimpleApp: In SimpleApp open views.py file then define home method 
  - In SimpleApp, create new urls.py file to manage SimpleApp
  - In SimpleApp, create a new URL pattern to link method home in views.py file
  - In NewProject, import include SimpleApp/urls.py on the sencond line of NewProject/urls.py
  - Working flow of url: access url: http://localhost:8000 --> NewProject/urls.py --> SimpleApp/urls --> home method
<p> The structure a app </p>
  ```
  SimpleApp/
      __init__.py
      admin.py
      apps.py
      migrations/
          __init__.py
      models.py
      tests.py
      views.py
  ```

  - migrations: update (add, delete, update) database schema when models change
  - admin.py: a configuration file for the built-in Django Admin app
  - apps.py: a configuration file for the app itself
  - models.py: where we define our database models which Django automatically translates into database tables
  - tests.py: test the working of the app
  - views.py: where we handle the request/response logic for our web app
<p> *Note: *__init__.py, urls.py  has the same function in NewProject but here it is in SimpleApp </p>

>>>
  *Project & apps*
  - A project represents the entire website whereas, an app is basically a submodule of the project.
  - A single project can contain multiple apps whereas, an app can also be used in different projects.
  - A project is like a blueprint of the entire web application whereas, apps are the building blocks of an web application.
  - We generally creates a single project for our website with one or more apps in it.
  - A project mantains configuration and settings realated to the whole web application. Apps on the other hand, can be independent or realted to one another.
>>>

>>>
* About path and include function*
  - Path:  function is passed four arguments, two required: route and view, and two optional: kwargs, and name
  - Include: function allows referencing other URLconfs
>>>
### Types of request and response
  - Type of request: HttpRequest attributes, HttpRequest method,  QueryDict
  - Type of response: HttpResponse attributes, HttpResponse method, HttpResponse subclasses, JsonResponse, StreamingHttpResponse, FileResponse  
# 3. Models + Database
####  List supported database engine:
   - django.db.backends.sqlite3 (default)
   - django.db.backends.postgresql
   - django.db.backends.mysql
   - django.db.backends.oracle
### Prepare:
- Create a new blog app + config (follow 2. Create a new app + URLs Mapping + Simple View )
- Create database with name "django_demo" (Here I use DBeaver tool to create database )

### Setting connection to database postgresql
  1. In *NewProject/settings.py: *change default sqlite3 to postgresql of DATABASES section
    ```py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'demoDjango',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
  
   


