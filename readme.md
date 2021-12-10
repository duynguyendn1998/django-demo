# Instruction
#### 1. What is Django?

  <p> Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.</p>

#### 2. Django MTV pattern
  - MTV: Model-Template-View
  - Model (M): Logical data structure
  - Template (T): Presentation layer
  - View (V): Data formatting
  - Working flow of Django framework: Template --> View --> Models --> View --> Template

**Require**: Let use Python3
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

> **Note** Name_project avoid using name like "Django" or "Test"
<p>Structure a project:</p>

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
  - In NewProject, import include SimpleApp/urls.py on the second line of NewProject/urls.py
  - Working flow of url: access url: http://localhost:8000 --> NewProject/urls.py --> SimpleApp/urls --> home method
<p> The structure a app: </p>

  ```shell script
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

**Note**:__init__.py, urls.py  has the same function in NewProject but here it is in SimpleApp

>>>
  **Project & apps**
  - A project represents the entire website whereas, an app is basically a submodule of the project.
  - A single project can contain multiple apps whereas, an app can also be used in different projects.
  - A project is like a blueprint of the entire web application whereas, apps are the building blocks of an web application.
  - We generally creates a single project for our website with one or more apps in it.
  - A project mantains configuration and settings realated to the whole web application. Apps on the other hand, can be independent or realted to one another.
>>>

>>>
  **About path and include function**
  - Path:  function is passed four arguments, two required: route and view, and two optional: kwargs, and name
  - Include: function allows referencing other URLconfs
>>>
### Types of request and response
  - Type of request: HttpRequest attributes, HttpRequest method,  QueryDict
  - Type of response: HttpResponse attributes, HttpResponse method, HttpResponse subclasses, JsonResponse, StreamingHttpResponse, FileResponse  
# 3. Models + Database
#### Prepare:
- Create a new blog app + config (follow 2. Create a new app + URLs Mapping + Simple View )
- Create database with name "django_demo" (Here I use DBeaver tool to create database )
- Install psycopg2 `$ pip install django psycopg2`
  > Once your virtual environment is active, you can install Django with pip. We will also install the psycopg2 package that will allow us to use the database we configured
### Models Field Types/Relationships
> **Models:** A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
#### Field types:
Each field in your model should be an instance of the appropriate Field class. Django uses the field class types to determine a few things:
- The column type, which tells the database what kind of data to store (e.g. INTEGER, VARCHAR, TEXT).
- The default HTML widget to use when rendering a form field.
- The minimal validation requirements, used in Django’s admin and in automatically-generated forms.

**Field options**
- null
- blank
- choices
- default
- help_text
- primary_key
- unique
#### Create users model
  1. In **blog/models.py**
  ``` shell script
  from django.db import models

  # Create Users models.
  class Users(models.Model):
      user_name = models.CharField(max_length=50, unique = True) # data type varchar with max_length 50 and unique value 
      email = models.CharField(max_length=100)
      password = models.CharField(max_length=50)
      created_dt = models.DateTimeField(auto_now_add=True) # data type timestamptz and auto add when insert row
  ```
#### Relationships
Django offers ways to define the three most common types of database relationships: many-to-one, many-to-many and one-to-one.  

**Many-to-one relationships**

To define a many-to-one relationship, use django.db.models.ForeignKey. 

ForeignKey requires a positional argument: the class to which the model is related.

  ``` shell script
  from django.db import models

  # Create Posts models.
  class Posts(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE, default="") # update to foreign key --> it is user_id in Posts table of database
    title = models.CharField(max_length=100)
    content_post = models.TextField() # data type text
    created_dt = models.DateTimeField(auto_now_add=True) 

  # Create Comments models.
  class Comments(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE, default="")  # update to foreign key --> it is user_id in Comments table of database
    post = models.ForeignKey(Posts,on_delete=models.CASCADE, default="")  # update to foreign key --> it is post_id in Comments table of database
    content_comment = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)
  ```
**Many-to-many relationships**

To define a many-to-many relationship, use ManyToManyField   
ManyToManyField requires a positional argument: the class to which the model is related.   

 Example:  
  ``` shell script
  from django.db import models

  class Topping(models.Model):
      # ...
      pass

  class Pizza(models.Model):
      # ...
      toppings = models.ManyToManyField(Topping)
  ```  
Reference [here](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/)   
**One-to-one relationships**   
To define a one-to-one relationship, use OneToOneField.   
OneToOneField requires a positional argument: the class to which the model is related.   
 Example:  
  ``` shell script
  from django.db import models

  class Person(models.Model):
      name = models.CharField(max_length=128)

      def __str__(self):
          return self.name

  class Group(models.Model):
      name = models.CharField(max_length=128)
      members = models.ManyToManyField(Person, through='Membership')

      def __str__(self):
          return self.name

  class Membership(models.Model):
      person = models.ForeignKey(Person, on_delete=models.CASCADE)
      group = models.ForeignKey(Group, on_delete=models.CASCADE)
      date_joined = models.DateField()
      invite_reason = models.CharField(max_length=64)
  ```  
Reference [here](https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one/)   

###  List supported database engine:
   - django.db.backends.sqlite3 (default)
   - django.db.backends.postgresql
   - django.db.backends.mysql
   - django.db.backends.oracle
#### Setting connection to database postgresql
  1. In *NewProject/settings.py*: change default sqlite3 to postgresql of DATABASES section
  >>>
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
  >>>
### What is the Migrations?
> **Migrations** are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They're designed to be mostly automatic, but you'll need to know when to make migrations, when to run them, and the common problems you might run into.

**Create file migrations**
In `..\NewProject>` run  `$ python manage.py makemigrations blog`
The result: 

``` shell script
  ...\NewProject> python manage.py makemigrations blog
  Migrations for 'blog':
    blog\migrations\0001_initial.py
      - Create model Comments
      - Create model Posts
      - Create model Users
```
I see a file to create in ...\NewProject\blog\migrations\0001_initial.py with content

``` shell script
  # Generated by Django 3.2.9 on 2021-12-02 12:10
  from django.db import migrations, models

  class Migration(migrations.Migration):

      initial = True

      dependencies = [
      ]

      operations = [
          migrations.CreateModel(
              name='Comments',
              fields=[
                  ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                  ('content_comment', models.TextField()),
                  ('created_dt', models.DateTimeField(auto_now_add=True)),
              ],
          ),
          migrations.CreateModel(
              name='Posts',
              fields=[
                  ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                  ('title', models.CharField(max_length=100)),
                  ('content_post', models.TextField()),
                  ('created_dt', models.DateTimeField(auto_now_add=True)),
              ],
          ),
          migrations.CreateModel(
              name='Users',
              fields=[
                  ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                  ('user_name', models.CharField(max_length=100)),
                  ('email', models.CharField(max_length=100)),
                  ('password', models.CharField(max_length=100)),
                  ('created_dt', models.DateTimeField(auto_now_add=True)),
              ],
          ),
      ]
```
**Run migrate to create those model tables in your database**
```shell script
  $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, blog, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying admin.0003_logentry_add_action_flag_choices... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
    missions... OK
      Applying auth.0012_alter_user_first_name_max_length... OK
      Applying blog.0001_initial... OK
      Applying sessions.0001_initial... OK
```
**When update models**
- Change models in models.py
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate to apply` those changes to the database. 

**Reversing migrate**
```shell script
  # migrate version 3
  ...\NewProject> python manage.py migrate blog
  Operations to perform:
    Apply all migrations: blog
  Running migrations:
    Applying blog.0003_alter_users_email... OK
  # reversing version 2
  ...\NewProject> python manage.py migrate blog 0002
  Operations to perform:
    Target specific migration: 0002_auto_20211203_0933, from blog
  Running migrations:
    Rendering model states... DONE
    Unapplying blog.0003_alter_users_email... OK
```  
> **Note**: It is possible to use multiple databases for a project, which can be found **[here](https://docs.djangoproject.com/en/3.2/topics/db/multi-db/).**   

# 4. Admin interface
> One of the most powerful parts of Django is the automatic admin interface. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for building your entire front end around.   

#### Add Django Admin into the project
The admin is enabled in the default project template used by startproject.  
#### Create superuser
`$ python manage.py createsuperuser`   
After entering the command, the system asks for admin account information, you usually enter username, email and password to initialize:  
#### Register your Models
In setting.py of blog app,  register model for admin page  

``` shell script
  from django.contrib import admin
  from .models import Posts, Comments

  # Setting display for Posts
  class PostAdmin(admin.ModelAdmin):
      list_display = ['title', 'created_dt'] # display column title & created_dt
      list_filter = ['created_dt'] # filter by created_dt column
      search_fields = ['title'] #  search by titel column

  admin.site.register(Posts, PostAdmin) # registion model with setting display PostAdmin
```   

#### Access to the Admin page
Now, Turn on the server and go to `/admin` and use the account I just created to log in.   

# 5. Django ORM And QuerySets
>>> 
Once you’ve created your data models, Django automatically gives you a database-abstraction API that lets you create, retrieve, update and delete objects.  
- Object-Relational Mapping (ORM)
- A QuerySet represents a collection of objects from your database. It can have zero, one or many filters. Filters narrow down the query results based on the given parameters. In SQL terms, a QuerySet equates to a SELECT statement, and a filter is a limiting clause such as WHERE or LIMIT. 
>>>   

#### Insert data to database  
`py .\manage.py shell` or write in `..\blog\models.py` (but run with way data insert each build again)
```shell scipt
  # Create data example for User
  >>> from blog.models  import Users 
  >>> u = Users(user_name= 'Tuong Duy', email='nptduy@tma.com.vn', password='12345678x@X')
  >>> u.save()
  # Create data example for post
  >>> from blog.models import Posts
  >>> p = Posts(user_id = 1, title = 'Making queries', content_post = 'Once you’ve created your data models, Django automatically gives you a database-abstraction API that lets you create, retrieve, update and delete objects. This document explains how to use this API. Refer to the data model reference for full details of all the various model lookup options.')
  >>> p.save()
  # Create data example for comment
  >>> from blog.models import Comments
  >>> c = Comments(user_id= 1, post_id = 3, content_comment = 'Hello') 
  >>> c.save()
```  
#### Methods that return new QuerySets  
**Get all object of Posts**   
``` shell script
  >>> from blog.models import Posts
  >>> Posts.objects.all()
```  
**filter()**   
Returns a new QuerySet containing objects that match the given lookup parameters.   
``` shell script
  # Get all post by user_id = 1
  >>> from blog.models import Posts
  >>> Posts.objects.filter(user_id=1)
  # get by year and user_id
  >>> Posts.objects.filter(user_id=1, created_dt__year = 2020)
```   
**exclude()**   
Returns a new QuerySet containing objects that do not match the given lookup parameters.   

``` shell script
  >>> from blog.models import Posts
  >>> Posts.objects.exclude(user_id=1)
```   
**order_by()**   
``` shell script
  >>> from blog.models import Posts
  # sort asc by id
  >>> Posts.objects.order_by('id')
  # sort desc by id
  >>> Posts.objects.order_by('-id')
```   
**Limiting QuerySets**   
``` shell script
  >>> from blog.models import Posts
  # return the first 2 objects of the table
  >>> Posts.objects.all()[:2]
  # returns from 2nd to 5th object 
  >>> Posts.objects.all()[2:5]
  # returns from 2nd
  >>> Posts.objects.all()[2]
```   
**Field lookups**    
get() takes only one object   
filter() takes multiple objects   

``` shell script
  >>> from blog.models import Posts
  # where title = 'hello world'
  >>> Posts.objects.get(title__exact='hello world')
  # where title = 'hello world' the same exact but case-insensitive 
  >>> Posts.objects.get(title__iexact='heLlo world')
  # where title like '%hello%'
  >>> Posts.objects.filter(title__contains='hello')
  # where title like '%hello%' the same contains but case-insensitive
  >>> Posts.objects.filter(title__icontains='heLlo')
  # where title like 'hello%' (istartswith: case-insensitive)
  >>> Posts.objects.filter(title__startswith='hello')
  # where title like '%hello' (iendswith: case-insensitive)
  >>> Posts.objects.filter(title__endswith='hello')
```   







