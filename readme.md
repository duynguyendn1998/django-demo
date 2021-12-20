# Instruction
#### 1. What is Django?

  <p> Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.</p>

#### 2. Django MTV pattern
 The MVT (Model View Template) is a software design pattern. It is a collection of three important components Model View and Template.  
  - Model (M) helps to handle database. It is a data access layer which handles the data. 
  - Template (T) is a presentation layer which handles User Interface part completely.    
  - View (V) is used to execute the business logic and interact with a model to carry data and renders a template.  


## Install 
**Require**: Let use Python3  
**Setting up a virtual environment**    
`...\> py -m venv django-demo`
**To activate the environment, run:**    
`...\> django-demo\Scripts\activate.bat`  
**Install django**  
Django can be installed easily using pip within your virtual environment.   
`...\> py -m pip install Django`   
**Check version django** (new in Django 3.2)     
`$ python -m django --version`    

# 1. Start new project
### Create a project
  ```shell script
      django-admin startproject helloworld
  ```
<p>This will create a helloworld directory in your current directory</p>

> **Note** Name_project avoid using name like "Django" or "Test"
<p>Structure a project:</p>

```shell script
helloworld/
    manage.py
    helloworld/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

<p>These files are:</p>
The outer helloworld/ root directory is a container for your project. Its name doesn’t matter to Django; can rename it to anything.   

  - helloworld: directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it
  - manage.py: used as a command-line utility for our projects (use for debugging, deploying and runing our  web applications)  
  - __init__.py: An empty file that tells Python that this directory should be considered a Python package.   
  - wsgi.py: (web server gateway interface) deploy project to server    
  - asgi.py: (Asynchronours server gateway interface) the same wsgi  
  - setting.py: project configuration  
  - urls.py: URLs of web pages to link web pages together   

#### Run server:
 - Run with port default: `python manage.py runserver`
 - Run with port 8080: `python manage.py runserver 8080`

# 2. Create a new app + URLs Mapping + Simple View
### Create a new app
  - In `...\helloworld>`,  `python manage.py startapp simple_apps`
  - In the helloworld project, open setting.py file add name_app (simple_app) to INSTALLED_APPS
  - Update setting for helloworld: In `...\helloworld>`: `python manage.py migrate`
### Define URL + simple views
  - Create simple views in simple_app: In simple_app open views.py file then define home method 
  - In simple_app, create new urls.py file to manage simple_app
  - In simple_app, create a new URL pattern to link method home in views.py file
  - In helloworld, import include simple_app/urls.py on the second line of helloworld/urls.py
  - Working flow of url: access url: http://localhost:8000 --> helloworld/urls.py --> simple_app/urls --> home method
<p> The structure a app: </p>

  ```shell script
  simple_app/
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

**Note**:__init__.py, urls.py  has the same function in helloworld but here it is in simple_app

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
  1. In *helloworld/settings.py*: change default sqlite3 to postgresql of DATABASES section
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
In `..\helloworld>` run  `$ python manage.py makemigrations blog`
The result: 

``` shell script
  ...\helloworld> python manage.py makemigrations blog
  Migrations for 'blog':
    blog\migrations\0001_initial.py
      - Create model Comments
      - Create model Posts
      - Create model Users
```
I see a file to create in ...\helloworld\blog\migrations\0001_initial.py with content

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
  ...\helloworld> python manage.py migrate blog
  Operations to perform:
    Apply all migrations: blog
  Running migrations:
    Applying blog.0003_alter_users_email... OK
  # reversing version 2
  ...\helloworld> python manage.py migrate blog 0002
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
**select_related**   
Returns a QuerySet that will “follow” foreign-key relationships, selecting additional related-object data when it executes its query. This is a performance booster which results in a single more complex query but means later use of foreign-key relationships won’t require database queries.   

`select_related(*fields)`  

**prefetch_related**   
Returns a QuerySet that will automatically retrieve, in a single batch, related objects for each of the specified lookups.  

`prefetch_related(*lookups)`

Reference select_related and prefetch_related in **[here](https://docs.djangoproject.com/en/3.2/ref/models/querysets/)**    

#### Response query data as json   

**serializers**   
```shell script
  from django.core import serializers
  from blog.models import Posts

  def parse_response_json(self):
        qs = Posts.objects.all()
        # get full queryset
        qs_json = serializers.serialize('json', qs)
        # only get field 'title','content_post' of fields
        qs_json = serializers.serialize('json', qs, fields=('title','content_post'))

        print(qs_json)
 
```
# 6. Templates + Static Files   
### The Django template language  
In blog app create new folder **templates**   
In template folder create new file **base.html** to define frame for page (ex: header, fooder,..)   
##### Variables 
A variable outputs a value from the context, which is a dict-like object mapping keys to values.   
Variables are surrounded by {{ and }} like this:   
In `.\blog\templates\display_variables.html`
``` html
  {% extends "base.html" %} <!-- extend layout of base.html -->

  {% block title %}Display variables{% endblock %}

  {% block content %}
      <li>Title: {{title}}</li>
      <li>Author: {{author}}</li>
      <li>Content_post: {{content_post}}</li>
  {% endblock %}
```  
In `.\blog\views.py`
```shell script
  def display_variables(request):
    # define dict example to display variables
    posts = {
        "title": "This is post", 
        "author": "Tuong Duy",
        "content_post": "Have a nice day!"
    }
   
    return render(request, "display_variables.html", posts)
```
In `.\blog\urls.py` add path:  `path('display_variables', views.display_variables)`   

##### Filters
Filters transform the values of variables and tag arguments.
In `.\blog\templates\display_variables.html`
```shell script
  {% extends "base.html" %} <!-- extend layout of base.html -->

  {% block title %}Display variables{% endblock %}

  {% block content %}
      <li>Title: {{title}}</li>
      <li>Author: {{author}}</li>
      <li>Content_post: {{content_post|lower|linebreaks }}</li> <!-- use filter break line -->
  {% endblock %}
```  

##### Tag
Tags provide arbitrary logic in the rendering process.  
Tags are surrounded by {% and %} like this:
In `.\blog\templates\display_variables.html`
```shell script
  {% extends "base.html" %} <!-- extend layout of base.html -->

  {% block title %}Display variables{% endblock %}

  {% block content %}
      <li>Title: {{title}}</li>
      <li>Author: {{author}}</li>
      <li>Content_post: {{content_post|lower|linebreaks }}</li> <!-- use filter break line -->
  {% endblock %}
```    
**Comment**   
Comments look like this:   
`{# this won't be rendered #}`  
A {% comment %} tag provides multi-line comments.

### Static file
Websites generally need to serve additional files such as images, JavaScript, or CSS. In Django, we refer to these files as “static files”. Django provides django.contrib.staticfiles to help you manage them.   
**Configuring static files**   
In **./helloworld/settings.py**   
**django.contrib.staticfiles** is included in your INSTALLED_APPS.   

```shell script
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = 'static/'
```      
STATICFILES_DIRS is a dict that stores folder paths containing static files.
``` shell script
  STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
  ]
```   
Create folder `./helloworld/static/images` to save image and saved a image   
In `./blog/templates/` create file load_image.html to test load static file    
``` shell script
  {% load static %}

  <img src="{% static 'images/tree.jfif' %}" alt="Tree"> 
```   
In `./blog/views.py` add method   
``` shell script
  def load_images(request):
    return render(request, "load_image.html")
```    
In `./blog/urls.py` add path: `path('load_images',views.load_images)`    
After run  `http://127.0.0.1:8000/blog/load_images` you see image saved   

>**Note**  
Django will use the first static file it finds whose name matches, and if you had a static file with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the best way to ensure this is by namespacing them. That is, by putting those static files inside another directory named for the application itself.
>    
#### Update template for posts list
Download boostrap **[here](https://getbootstrap.com/)** after unzip and put in the static folder.  
In `./blog/templates/base.html` add link:
`<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}" type="text/css">` to all page extends base.html do not import again   
In `./blog/views.py` add method   
``` shell script
  def blogs_list(request):
    Data = {'Posts': Posts.objects.all().order_by('-created_dt')}
    return render(request, 'blog_list.html', Data)
```     
In `./blog/urls.py` add path: `path('',views.blogs_list)`   
In `./blog/templates/` create file blog_list.html 
``` shell script
{% extends "base.html" %}
{% load static %}
{% block title %}Blog{% endblock %}
{% block content %}
<div class="card-deck">
    {% for post in Posts %}
        <div class="card" style="width: 18rem;">
            <img class="card-img-top" src="{% static 'images/tree.png' %}" alt="blog image">
            <div class="card-body">
                <h5 class="card-title">{{post.title}}</h5>
                <p class="card-text">{{post.created_dt|date:"d-m-Y"}}.</p>
                <a href="#" class="btn btn-primary">View detail</a>
            </div>
        </div>
    {% endfor %}
</div>
{% endblock %}
```    
# 7. Use generic views + Forms










